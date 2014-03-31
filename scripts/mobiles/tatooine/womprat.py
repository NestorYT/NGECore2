import sys
from services.spawn import MobileTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	templates = Vector()
	templates.add('object/mobile/shared_womp_rat.iff')
	mobileTemplate.setCustomName('a womp rat')
	mobileTemplate.setTemplates(templates)
	mobileTemplate.setLevel(5)
	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	core.spawnService.addMobileTemplate('womprat', mobileTemplate)
	
