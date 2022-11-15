import React from 'react';
import clsx from 'clsx';

const ContentDiv = props => {
    const {title, checks, isRight, id} = props;
    return (
        <div id={id} className={clsx('col', 'col--6', 'padding-top--md', 'margin-bottom--md')}>
            <div className={clsx('row')}>
                <div className={clsx('col col--11 padding-top--md', isRight ? 'col--offset-1' : '')}>
                    <h1 className={clsx('margin-bottom--sm')}>{title}</h1>
                    <ul style={{listStyleType: 'none', paddingLeft: 0}}>
                        {
                            checks.map(check => (
                                <div className={clsx('row')}>
                                    <div className={clsx('col', 'col--12')}>
                                        <li>
                                            <span style={{fontSize: '2rem', color: 'green', verticalAlign: 'middle'}}>
                                                <i class="fas fa-check-circle"></i>
                                            </span>
                                            <span style={{ marginLeft: '1rem', fontSize: '20px' }}>{check}</span>
                                        </li>
                                    </div>                                                            
                                </div>
                            ))
                        }
                    </ul>
                </div>
            </div>  
        </div>
    );
};

export default ContentDiv;