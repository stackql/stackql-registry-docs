import React from 'react';
import clsx from 'clsx';
import styles from './animatedterm.module.css';
import Code from '../Code';

const AnimatedTerm = props => {
    const { data } = props;
    return (
        <section className={clsx(styles.macSection)}>
            <div className={clsx(styles.macDiv)}>
                <div className={clsx(styles.marvelDevice, styles.macbook)}>
                    <div className={clsx(styles.notch)}>
                        <div className={clsx(styles.camera)}></div>
                        <div className={clsx(styles.speaker)}></div>
                    </div>
                    <div className={clsx(styles.topBar)}></div>
                    <div className={clsx(styles.sleep)}></div>
                    <div className={clsx(styles.bottomBar)}></div>
                    <div className={clsx(styles.volume)}></div>
                    <div className={clsx(styles.screen)}>
                        <Code data={data} />
                    </div>
                </div>
            </div>
        </section>
    );
};
    
export default AnimatedTerm;