import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import '@fortawesome/fontawesome-free/css/all.css';
import useBaseUrl from '@docusaurus/useBaseUrl';

const DocumentationLink = props => {
  const { styles } = props;
  const docs = useBaseUrl('/docs');
  const docIcon = 'fa-solid fa-book';
  return(
    <Link
    className={clsx('button', styles ? styles : 'button--outline button--primary')}
    to={docs}>
    <span><i class={docIcon}></i></span>&nbsp;&nbsp;Read the Docs
    </Link>
  );
};

export default DocumentationLink;