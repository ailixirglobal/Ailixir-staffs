from django.db import models
from django.contrib.auth import get_user_model
from research.models import Experiment
from product.models import Product

User = get_user_model()


class AIUserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="ai_settings")

    # Optional system prompt (custom behavior)
    system_prompt = models.TextField(blank=True, null=True)

    # Attach one experiment for research-based AI responses
    active_experiment = models.ForeignKey(
        Experiment,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="ai_users",
        help_text="If selected, AI will use this experiment's description and lab notes as context."
    )

    # Attach multiple products to AI context
    context_products = models.ManyToManyField(
        Product,
        blank=True,
        related_name="ai_context_users",
        help_text="AI will reference these products during responses."
    )

    # Base controls
    ai_model = models.CharField(max_length=100, default="openai/gpt-oss-20b:groq")
    temperature = models.FloatField(default=0.7)
    max_tokens = models.IntegerField(default=300)

    use_history = models.BooleanField(default=True)
    use_role_context = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"AI Settings for {self.user.username}"
  
  
class ChatSession(models.Model):
    """
    Represents a conversation session between a user and the AI.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_sessions')
    session_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatSession {self.session_id} ({self.user.username})"
        


class Message(models.Model):
    """
    Represents an individual message in a chat session.
    """
    ROLE_CHOICES = [
        ('user', 'User'),
        ('assistant', 'Assistant'),
    ]

    chat_session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role.upper()} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"