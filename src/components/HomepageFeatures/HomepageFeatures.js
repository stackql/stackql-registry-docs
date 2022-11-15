import React from 'react';
import clsx from 'clsx';

import styles from './homepagefeatures.module.css';

function Feature({icon, link, title, description}) {
  return (
    <div className={clsx('col', 'col--4', styles.featureDiv)}>
      <div className={clsx('padding-horiz--md')}>
        <h3><span className={clsx(icon, styles.featureIcon)}></span>{' '}{title}</h3>
        <p>{description}</p>
      </div>
      <div className={clsx('padding-horiz--md', styles.learnMore)}>
        <a href={link} className={clsx(styles.learnMoreLink)}>
          <span>Learn more <i class="fas fa-angle-double-right"></i></span> 
        </a>
      </div>
    </div>
  );
}

const HomepageFeatures = props => {
  const { data } = props;
  return (
    <section className={clsx(styles.features)}>
      <div className={clsx('container')}>
        <div className={clsx('row')}>
          {data.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
};

export default HomepageFeatures;