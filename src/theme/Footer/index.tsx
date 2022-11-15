/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

import React from 'react';
import clsx from 'clsx';

import Link from '@docusaurus/Link';
import {FooterLinkItem, useThemeConfig} from '@docusaurus/theme-common';
import useBaseUrl from '@docusaurus/useBaseUrl';
import isInternalUrl from '@docusaurus/isInternalUrl';
import styles from './styles.module.css';
import ThemedImage, {Props as ThemedImageProps} from '@theme/ThemedImage';
import IconExternalLink from '@theme/Icon/ExternalLink';
import { IconButton } from '@mui/material';
import { useColorMode } from '@docusaurus/theme-common';

import { Icon } from '@iconify/react';

function FooterLink({
  to,
  href,
  label,
  prependBaseUrlToHref,
  ...props
}: FooterLinkItem) {
  const toUrl = useBaseUrl(to);
  const normalizedHref = useBaseUrl(href, {forcePrependBaseUrl: true});

  return (
    <Link
      className="footer__link-item"
      {...(href
        ? {
            href: prependBaseUrlToHref ? normalizedHref : href,
          }
        : {
            to: toUrl,
          })}
      {...props}>
      {href && !isInternalUrl(href) ? (
        <span>
          {label}
          <IconExternalLink />
        </span>
      ) : (
        label
      )}
    </Link>
  );
}

const FooterLogo = ({
  sources,
  alt,
  width,
  height,
}: Pick<ThemedImageProps, 'sources' | 'alt' | 'width' | 'height'>) => (
  <ThemedImage
    className="footer__logo"
    alt={alt}
    sources={sources}
    width={width}
    height={height}
  />
);

function Footer(): JSX.Element | null {
  const socialLinks = {
    linkedin: "https://www.linkedin.com/company/stackql",
    twitter: "https://twitter.com/stackql",
    github: "https://github.com/stackql",
    discord: "https://discord.com/invite/xVXZ9d5NxN",
    slack: "https://join.slack.com/t/stackqlcommunity/shared_invite/zt-1cbdq9s5v-CkY65IMAesCgFqjN6FU6hg",    
  };
  
  // const { colorMode === 'dark' } = useThemeContext();
  const {colorMode} = useColorMode();

  const {footer} = useThemeConfig();

  const {copyright, links = [], logo = {}} = footer || {};
  const sources = {
    light: useBaseUrl(logo.src),
    dark: useBaseUrl(logo.srcDark || logo.src),
  };

  if (!footer) {
    return null;
  }

  return (
    <footer
      className={clsx('footer', {
        'footer--dark': footer.style === 'dark',
      })}
    >
      <div className="container">
        {links && links.length > 0 && (
          <div className="row footer__links">
            <div className="col col--6 footer__col">
              {logo && (logo.src || logo.srcDark) && (
                <div className="margin-bottom--sm">
                  {logo.href ? (
                    <Link href={logo.href} className={styles.footerLogoLink}>
                      <FooterLogo alt={logo.alt} sources={sources} />
                    </Link>
                  ) : (
                    <FooterLogo alt={logo.alt} sources={sources} />
                  )}
                </div>
              )}
              <p className="footer__subtitle">
                A new approach to querying and <br />
                provisioning cloud services.
              </p>
            </div>
            {links.map((linkItem, i) => (
              <div key={i} className="col footer__col">
                {linkItem.title != null ? (
                  <h4 className="footer__title">{linkItem.title}</h4>
                ) : null}
                {linkItem.items != null &&
                Array.isArray(linkItem.items) &&
                linkItem.items.length > 0 ? (
                  <ul className="footer__items">
                    {linkItem.items.map((item, key) =>
                      item.html ? (
                        <li
                          key={key}
                          className="footer__item" // Developer provided the HTML, so assume it's safe.
                          // eslint-disable-next-line react/no-danger
                          dangerouslySetInnerHTML={{
                            __html: item.html,
                          }}
                        />
                      ) : (
                        <li key={item.href || item.to} className="footer__item">
                          <FooterLink {...item} />
                        </li>
                      ),
                    )}
                  </ul>
                ) : null}
              </div>
            ))}
          </div>
        )}
        <div className="divider" />
        {(logo || copyright) && (
          <>
          <div className="footer__bottom text--center">
            {copyright ? (
              <div
                className="footer__copyright" // Developer provided the HTML, so assume it's safe.
                // eslint-disable-next-line react/no-danger
                dangerouslySetInnerHTML={{
                  __html: copyright,
                }}
              />
            ) : null}
          </div>
          <div className="footer__bottom text--center">
          <IconButton
            className="footerSocialIconButton"
            href={socialLinks.github}
            size="large"
            target="_blank"
            rel="noopener"
            >
              <Icon icon="akar-icons:github-fill" width="24" color={colorMode === 'dark' ? 'white' : ''} />
          </IconButton>
          <IconButton
            className="footerSocialIconButton"
            href={socialLinks.twitter}
            size="large"
            target="_blank"
            rel="noopener"
            >
              <Icon icon="akar-icons:twitter-fill" width="24" color={colorMode === 'dark' ? 'white' : ''} />
          </IconButton>
          <IconButton
            className="footerSocialIconButton"
            href={socialLinks.linkedin}
            size="large"
            target="_blank"
            rel="noopener"
            >
              <Icon icon="fa:linkedin-square" width="24" color={colorMode === 'dark' ? 'white' : ''} />
          </IconButton>     
          <IconButton
            className="footerSocialIconButton"
            href={socialLinks.discord}
            size="large"
            target="_blank"
            rel="noopener"
            >
            <Icon icon="mdi:discord" color={colorMode === 'dark' ? 'white' : ''} />
          </IconButton>
          <IconButton
            className="footerSocialIconButton"
            href={socialLinks.slack}
            size="large"
            target="_blank"
            rel="noopener"
            >
              <Icon icon="fa:slack" width="24" color={colorMode === 'dark' ? 'white' : ''} />
          </IconButton>          
          </div>
          </>
        )}
      </div>
    </footer>
  );
}

export default Footer;
