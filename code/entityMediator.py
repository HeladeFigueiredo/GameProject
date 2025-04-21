# Gerencia as colisões
from code.enemy import Enemy
from code.entity import Entity


class EntityMediator:

    # Verifica se o inimigo atingiu o limite da tela
    # O __ significa que o metodo e privado e so pode ser usado dentro da propria classe
    @staticmethod
    def __verify_collision_windown(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_windown(test_entity)

    # Metodo que destroi a entidade quando a vida zerar
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
