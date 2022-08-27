'use strict'

import { getConfig } from './config.js'
import BaseScene from './scene/baseScene.js'


const config = getConfig()
config.scene = [BaseScene]
new Phaser.Game(config);