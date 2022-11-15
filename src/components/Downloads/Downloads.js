import React from 'react';
import clsx from 'clsx';
import {
  DownloadCard,
} from '../../components';

import styles from './downloads.module.css';

function Download({platform, icon, title, description, buttons}) {
  let cardData = {
    platform: platform, 
    icon: icon, 
    description: description, 
    buttons: buttons,
  };
  return (
    <div className={clsx('col', 'col--4', styles.downloadDiv)}>
      <DownloadCard
          key={title}
          data={cardData}
          liftUp
      />
    </div>
  );
}

const Downloads = props => {
  const { data } = props;
  return (
    <section className={clsx(styles.downloads)}>
      <div className={clsx('container')}>
        <div className={clsx('row')}>
          {data.map((props, idx) => (
            <Download key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
};

export default Downloads;