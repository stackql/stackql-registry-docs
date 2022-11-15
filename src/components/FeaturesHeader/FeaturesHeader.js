import React from 'react';
import clsx from 'clsx';
import MediaQuery from 'react-responsive';
import {
  SectionHeader,
  DownloadLink,
  DocumentationLink,
} from '../../components';
import {
    Card,
} from './components';

import buttonStyles from '../Hero/hero.module.css';
import styles from './featuresheader.module.css';

const FeaturesSectionHeader = props => {
    const { title, subtitle, label } = props;
    return (
        <SectionHeader
        title={title}
        subtitle={subtitle}
        align="left"
        label={label}
        ctaGroup = {[
            <MediaQuery minWidth={1224}>
            <div className={clsx(buttonStyles.buttons)}>
                <DownloadLink styles={['button--primary']}/>
            </div>
            </MediaQuery>,
            <MediaQuery minWidth={1224}>
            <div style={{width: "2em"}}></div>
            </MediaQuery>,
            <div className={clsx(buttonStyles.buttons)}>
            <DocumentationLink />
            </div>
        ]}
    />
    );
};

const FeatureCards = props => {
    const { cards } = props;
    return (
        <div className={clsx('row')}>
        <div className={clsx('col', 'col--2')}></div>
        <div className={clsx('col', 'col--5', styles.cardsLeftCol)}>
            <div className={clsx('row', 'margin-bottom--md', 'margin-right--sm')}>
                <Card data={cards[0]} liftUp />
            </div>
            <div className={clsx('row', 'margin-right--sm')}>
                <Card data={cards[1]} liftUp />
            </div>
        </div>
        <div className={clsx('col', 'col--5', styles.cardsRightCol)}>
            <div className={clsx('row', 'margin-bottom--md', 'margin-right--sm')}>
                <Card data={cards[2]} liftUp />
            </div>
            <div className={clsx('row', 'margin-right--sm')}>
                <Card data={cards[3]} liftUp />
            </div>                            
        </div>
        </div>
    );
};

const FeatureCardsTabletViewport = props => {
    const { cards } = props;
    return (
        <>
        <div className={clsx('row', 'margin-vert--md')}>
            <div className={clsx('col475pct')}>
                <Card data={cards[0]} liftUp />
            </div>
            <div className={clsx('col5pct')}></div>
            <div className={clsx('col475pct')}>
                <Card data={cards[1]} liftUp />
            </div>
        </div>
        <div className={clsx('row', 'margin-vert--md')}>
            <div className={clsx('col475pct')}>
                <Card data={cards[2]} liftUp />
            </div>
            <div className={clsx('col5pct')}></div>            
            <div className={clsx('col475pct')}>
                <Card data={cards[3]} liftUp />
            </div>                        
        </div>
        </>
    );
};

const FeatureCardsMobileViewport = props => {
    const { cards } = props;
    return (
        <>
        <div className={clsx('mobileContainer')}>
            <div className={clsx('row', 'margin-bottom--lg')}>
            <Card data={cards[0]} liftUp />
            </div>
            <div className={clsx('row', 'margin-bottom--lg')}>
            <Card data={cards[1]} liftUp />
            </div>
            <div className={clsx('row', 'margin-bottom--lg')}>
            <Card data={cards[2]} liftUp />
            </div>
            <div className={clsx('row')}>
            <Card data={cards[3]} liftUp />
            </div>                                    
        </div>
        </>
    );
};

const FeaturesHeader = props => {
    const { data } = props;
    return (    
        <>
        {/* desktop layout */}
        <MediaQuery minWidth={997}>
        <div className={clsx('col', 'col--12')}>
            <div className={clsx('row')}>
                <div className={clsx('col', 'col--6', styles.cardsContainer)}>
                    <FeatureCards cards={data.cards} />
                </div>
                <div className={clsx('col', 'col--6')}>
                <div className={clsx('row')} style={{height: '20%'}}></div>
                <div className={clsx('row')}>
                    <FeaturesSectionHeader 
                    title={data.title}
                    subtitle={data.subtitle}
                    label={data.label}
                    />
                </div>
                </div>
            </div>
        </div>
        </MediaQuery>

        {/* mobile/small viewport layout */}
        <MediaQuery maxWidth={997}>
        <div className={clsx('row', 'margin-horiz--xs')}>
            <FeaturesSectionHeader 
            title={data.title}
            subtitle={data.subtitle}
            label={data.label}
            />
        </div>
        </MediaQuery>
        
        <MediaQuery minWidth={481} maxWidth={997}>
        <div className={clsx('row')}>
            <div className={clsx('mobileContainer')}>
                <FeatureCardsTabletViewport cards={data.cards} />
            </div>    
        </div>
        </MediaQuery>

        <MediaQuery maxWidth={480}>
        <div className={clsx('row')}>
            <div className={clsx('mobileContainer')}>
                <FeatureCardsMobileViewport cards={data.cards} />
            </div>    
        </div>
        </MediaQuery>
        </>
    );
};

export default FeaturesHeader;