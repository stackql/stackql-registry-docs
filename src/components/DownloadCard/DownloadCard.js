import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import '@fortawesome/fontawesome-free/css/all.css';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './downloadcard.module.css';

const DownloadCard = props => {
  const { data, liftUp } = props;
  return(
    <div className={clsx('card', 'card--full-height', styles.downloadCard, liftUp ? styles.downloadCardLift : '')}>
    <div className={clsx('card__header')}>
      <div className={clsx('avatar', 'avatar--vertical')}>
        <span className={clsx(styles.downloadIcon)}><i class={data.icon}></i></span>
        <div className={clsx('avatar__intro')}>
          <span className={clsx(styles.downloadTitle)}>{data.title}</span>
          <p className={clsx(styles.downloadDesc)}>{data.description}</p>
        </div>
      </div>
    </div>
    {/*
    <div className="card__body text--center">{data.description}</div>
    */}
    <div className={clsx('card__footer')}>
      <div className={clsx('button-group', 'button-group--block')}>
        {data.buttons.map(button => (
          <Link
          className={clsx('button', 'button--primary button--sm')}
          to={useBaseUrl(button.url)}>
          <span><i class={button.icon}></i></span>&nbsp;&nbsp;{button.text}
          </Link>
        ))}
      </div>
    </div>
  </div>
  );
};

export default DownloadCard;