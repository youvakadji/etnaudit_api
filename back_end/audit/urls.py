# urls.py
from django.urls import path

from .views.notificationViews import CreateNotificationView, GetNotificationView, NotificationListView
from .views.userViews import DeleteUserView, GetUserView, LoginView, SignupView, UpdateUserView, UserListView
from .views.promptViews import PromptListView, addPromptView, deletePromptView, getPromptView
from .views.auditViews import AuditCreateView, AuditListView, deleteAuditView, getAuditView, getPromptAndAIRecommendationByAudit
from .views.auditResultViews import AuditResultListView, deleteAuditResultView, getAuditResultByAuditIdView, getAuditResultView, saveResultView
from .views.logViews import LogListView, createLog, deleteLogView, getLogView
from .views.reportViews import ReportListView, GenerateReport, GetAnalysisView
from .views.aiRecommendationViews import AIRecommendationListView, addAIRecommendation, deleteAIRecommendation, getAIRecommendation, getAIRecommendationByPrompt

urlpatterns = [
    # Users and authentication
    path('users/', UserListView.as_view(), name='user-list'),
    path('user/', GetUserView.as_view(), name='user-detail'),
    path('user/update/', UpdateUserView.as_view(), name='user-update'),
    path('user/delete/', DeleteUserView.as_view(), name='user-delete'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    

    # Notifications
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/create/', CreateNotificationView.as_view(), name='create-notification'),
    path('notifications/<int:pk>/', GetNotificationView.as_view(), name='get-notification'),

    # Prompt 
    path('prompts/', PromptListView.as_view(), name='prompt-list-create'),
    path('prompts/<int:pk>/', getPromptView.as_view(), name='prompt-detail'),
    path('prompts/add/', addPromptView.as_view(), name='prompt-add'),
    path('prompts/delete/<int:pk>/', deletePromptView.as_view(), name='prompt-delete'),

    # Audit 
    path('audits/', AuditListView.as_view(), name='audit_list_create'),
    path('audits/<int:pk>/', getAuditView.as_view(), name='audit_detail'),
    path('audit/<int:audit>/prompt-ai-recommendation/', getPromptAndAIRecommendationByAudit.as_view(), name='prompt-ai-recommendation-by-audit'),
    path('audits/add/', AuditCreateView.as_view(), name='audit_add'),
    path('audits/delete/<int:pk>/', deleteAuditView.as_view(), name='audit_delete'),

    # Audit Result 
    path('audit-results/', AuditResultListView.as_view(), name='audit-result-list-create'),
    path('audit-results/<int:pk>/', saveResultView.as_view(), name='audit-result-add'),
    path('audit-results/<int:pk>/', getAuditResultView.as_view(), name='audit-result-detail'),
    path('audit-results/<int:audit_id>/', getAuditResultByAuditIdView.as_view(), name='audit-result-by-audit'),
    path('audit-results/delete/<int:pk>/', deleteAuditResultView.as_view(), name='audit-result-delete'),

    # Log 
    path('logs/', LogListView.as_view(), name='log-list-create'),
    path('logs/<int:pk>/', getLogView.as_view(), name='log-detail'),
    path('logs/create/', createLog.as_view(), name='log-create'),
    path('logs/delete/<int:pk>/', deleteLogView.as_view(), name='log-delete'),

    # Report 
    path('reports/', ReportListView.as_view(), name='report-list-create'),
    path('reports/<int:pk>/', GetAnalysisView.as_view(), name='get-analysis'),
    path('reports/generate/', GenerateReport.as_view(), name='report-generate'),

    # AI Recommendation 
    path('ai-recommendations/', AIRecommendationListView.as_view(), name='ai-recommendation-list-create'),
    path('ai-recommendations/<int:pk>/', getAIRecommendation.as_view(), name='ai-recommendation-detail'),
    path('ai-recommendations/<int:prompt_id>/', getAIRecommendationByPrompt.as_view(), name='ai-recommendation-by-audit'),
    path('ai-recommendations/add/', addAIRecommendation.as_view(), name='ai-recommendation-add'),
    path('ai-recommendations/delete/<int:pk>/', deleteAIRecommendation.as_view(), name='ai-recommendation-delete'),

]