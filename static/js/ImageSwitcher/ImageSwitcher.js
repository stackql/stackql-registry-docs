import React from 'react';
import Image from '@theme/IdealImage';
//import useThemeContext from '@theme/hooks/useThemeContext'; //docs: https://v2.docusaurus.io/docs/2.0.0-alpha.69/theme-classic#usethemecontext
import { useColorMode } from '@docusaurus/theme-common';

const ImageSwitcher = ({lightImageSrc, darkImageSrc, alttext}) => {
  //const { isDarkTheme } = useThemeContext();
  const {colorMode} = useColorMode();
  return (
    <Image img={colorMode === 'dark' ? darkImageSrc : lightImageSrc} alt={alttext} onClick={()=> window.open(lightImageSrc, "_blank")} />
  )
}

export default ImageSwitcher;