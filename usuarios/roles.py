from rolepermissions.roles import AbstractUserRole

class Coordenador(AbstractUserRole):
    available_permissions = {
        'add_ticket': True,
        'can_view_ticket': True,
        'can_close_ticket': True,
        'can_add_user': True,
        'can_view_user': True,
        'can_delete_user': True
        }

class Tecnico(AbstractUserRole):
    available_permissions = {
        'can_close_ticket': True,
        'can_view_ticket': True,
    }
    
class Profissional(AbstractUserRole):
    available_permissions = {
        'add_ticket': True,
        'can_view_ticket': True,
    }    
        