import React from 'react';
import clsx from 'clsx';
import styles from './card.module.css';
import AnchorLink from 'react-anchor-link-smooth-scroll'

const Card = props => {
    const { data, liftUp } = props;
    return (
        <div className={clsx('card', 'card--full-height', styles.featureCard, liftUp ? styles.featureCardLift : '')}>
            <div className={clsx('row')} style={{ padding: '8px', height: '42px' }}>
                <div className={clsx('col', 'col--2')}>
                    <div className={clsx(styles.featureIconContainer)}>
                        <span className={clsx(data.icon, styles.featureIcon)}></span>
                    </div>
                </div>
                <div className={clsx('col', 'col--10')}></div>
            </div>
            <div className={clsx('row')} style={{ padding: '8px' }}>
                <div className={clsx('col', 'col--12', 'padding-horiz--md', styles.featureTitle)}>
                {data.title}
                </div>
            </div>
            <div className={clsx('row')} style={{ padding: '8px' }}>
                <div className={clsx('col', 'col--12', 'padding-horiz--md', styles.featureText)}>
                    {data.text}        
                </div> 
            </div>   
            <div className={clsx('row')} style={{ padding: '8px' }}>
                <div className={clsx('col', 'padding-horiz--md', styles.learnMore)}>
                <AnchorLink className={clsx(styles.learnMoreLink)} href={data.link}>
                <span>Learn more <i class="fas fa-angle-double-right"></i></span> 
                </AnchorLink>
                </div>
            </div>
        </div>
    );
};

export default Card;