import React from 'react';
import clsx from 'clsx';
import {
    CodeDiv,
    ContentDiv,
} from './components';
import AOS from 'aos';
import 'aos/dist/aos.css';
import MediaQuery from 'react-responsive';

import styles from './featurescontent.module.css';

const FeatureContent = props => {
    const { feature, idx } = props;
    return (
        <>
        <MediaQuery minWidth={997}>
        <div className={clsx('row')}>
            {idx % 2 == 0 ? 
                <>
                <CodeDiv code={feature.code} />
                <ContentDiv id={feature.id} title={feature.title} checks={feature.checks} isRight/>
                </>
            : 
                <>
                <ContentDiv id={feature.id} title={feature.title} checks={feature.checks}/>            
                <CodeDiv code={feature.code} isRight/>
                </>
            }
        </div>
        </MediaQuery>
        <MediaQuery maxWidth={996}>
        <div className={clsx('row')}>
        <div className={clsx('mobileContainer')}>
        <ContentDiv id={feature.id} title={feature.title} checks={feature.checks} isRight/>
        </div>    
        </div>
        <div className={clsx('row')}>
        <div className={clsx('mobileContainer')}>
        <CodeDiv code={feature.code} isRight/>
        </div>
        </div>        
        </MediaQuery>
        </>
    );
};

const FeaturesContent = props => {
    const { data } = props;
    React.useEffect(() => {
        AOS.init({
          delay: 50,
          duration: 500,
          easing: 'ease-in-out',
          // disable: 'mobile',
        });
      }, []);    

    return (
        <>
        <div className={clsx('margin-top--xl', 'lgContainer')}>
            <div className={clsx('row')}>
                <>
                <div className={clsx('col', 'col--2')}></div>
                <div className={clsx('col', 'col--8')}>
                <div className={clsx('row')}>
                    <div className={clsx('col', 'col--12', styles.title)} dangerouslySetInnerHTML={{__html: data.title}} />
                </div>
                <div className={clsx('row')}>
                    <div className={clsx('col', 'col--12', 'margin-bottom--lg', styles.subtitle)}>
                        {data.subtitle}
                    </div>
                </div>
                {
                    data.features.map((feature, idx) => (
                        <FeatureContent feature={feature} idx={idx} />
                    ))
                }
                </div>
                <div className={clsx('col', 'col--2')}></div>
                </>
            </div>
        </div>
        </>
        );
    };
    
export default FeaturesContent;