import datetime
from src.config import db

class FeatureToggleSettings(db.Model):
    __tablename__ = 'feature_toggle_settings'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # Feature Toggles
    is_cpu_info_enabled = db.Column(db.Boolean, default=True)
    is_memory_info_enabled = db.Column(db.Boolean, default=True)
    is_disk_info_enabled = db.Column(db.Boolean, default=True)
    is_network_info_enabled = db.Column(db.Boolean, default=True)
    is_process_info_enabled = db.Column(db.Boolean, default=True)
    refresh_interval = db.Column(db.Integer, default=10)

