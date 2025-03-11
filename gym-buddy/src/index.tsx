import { root } from '@lynx-js/react'

import { App } from './App.js'
import { LoginPage } from './Login.jsx'

root.render(<LoginPage />)

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
}
