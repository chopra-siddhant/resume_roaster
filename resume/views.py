from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Resume, HRSimulator, LinkedInFlex
from .serializers import ResumeSerializer, HRSimulatorSerializer, LinkedInFlexSerializer
from .nlp_model import generate_roast, generate_improvements, generate_professional_improvements
from .utils import parse_resume

@api_view(['POST'])
def upload_resume(request):
    file_obj = request.FILES.get('resume')
    if not file_obj:
        return Response({"error": "No file provided"}, status=400)
    
    resume_text = parse_resume(file_obj)
    mode = request.POST.get('mode', 'humorous')  # default to humorous

    if mode == 'humorous':
        roast = generate_roast(resume_text)
        improvements = generate_improvements(resume_text)
    elif mode == 'professional':
        # In professional mode, we might choose to skip the roast or provide a toned review.
        roast = "Professional Review: The resume is well-structured."  # placeholder or call a dedicated function if desired.
        improvements = generate_professional_improvements(resume_text)
    else:
        roast = generate_roast(resume_text)
        improvements = generate_improvements(resume_text)
    
    resume_instance = Resume.objects.create(
        resume_text=resume_text,
        roast_result=roast,
        improvement_suggestions=improvements,
        user_email=request.POST.get('email', '')
    )
    
    serializer = ResumeSerializer(resume_instance)
    return Response(serializer.data)

@api_view(['GET'])
def get_resume_results(request, resume_id):
    try:
        resume_instance = Resume.objects.get(id=resume_id)
    except Resume.DoesNotExist:
        return Response({"error": "Resume not found"}, status=404)
    
    serializer = ResumeSerializer(resume_instance)
    return Response(serializer.data)

@api_view(['POST'])
def hr_simulator(request):
    resume_id = request.data.get('resume_id')
    try:
        resume_instance = Resume.objects.get(id=resume_id)
    except Resume.DoesNotExist:
        return Response({"error": "Resume not found"}, status=404)
    
    # Generate HR feedback (for demonstration, we reuse a roast-style generation)
    hr_feedback = f"HR Feedback: {generate_roast(resume_instance.resume_text)}"
    hr_instance = HRSimulator.objects.create(resume=resume_instance, hr_feedback=hr_feedback)
    serializer = HRSimulatorSerializer(hr_instance)
    return Response(serializer.data)

@api_view(['POST'])
def linkedin_flex(request):
    resume_id = request.data.get('resume_id')
    try:
        resume_instance = Resume.objects.get(id=resume_id)
    except Resume.DoesNotExist:
        return Response({"error": "Resume not found"}, status=404)
    
    # Generate a LinkedIn-style post using the improvement suggestions.
    generated_post = f"LinkedIn Flex Post: {generate_improvements(resume_instance.resume_text)}"
    linkedin_instance = LinkedInFlex.objects.create(resume=resume_instance, generated_post=generated_post)
    serializer = LinkedInFlexSerializer(linkedin_instance)
    return Response(serializer.data)
