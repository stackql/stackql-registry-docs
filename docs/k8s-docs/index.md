---
title: k8s
hide_title: false
hide_table_of_contents: false
keywords:
  - k8s
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Kubernetes resources using SQL
custom_edit_url: null
image: /img/providers/k8s/stackql-k8s-provider-featured-image.png
id: k8s-doc
slug: /providers/k8s
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Open source container management platform.  
    
:::info Provider Summary (v23.03.00121)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>5</b></span><br />
<span>total methods:&nbsp;<b>267</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>33</b></span><br />
<span>total selectable resources:&nbsp;<b>24</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `k8s` provider, run the following command:  

```bash
REGISTRY PULL k8s;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication


:::note

<b><CopyableCode code="cluster_addr" /></b> is a required parameter for all operations using the <code>k8s</code> provider, for example:  

```sql
SELECT name, namespace, uid, creationTimestamp 
FROM k8s.core_v1.service_account 
WHERE cluster_addr = '35.244.65.136' AND namespace = 'kube-system' 
ORDER BY name ASC;
```
:::

### Example using `kubectl proxy`
`kubectl proxy` is the default authentication method for the `k8s` provider, no other variables or configuration is necessary to query the `k8s` provider if you are using this method.  

:::note

The <CopyableCode code="protocol" /> parameter is required when accessing a Kubernetes cluster via `kubectl proxy`, see the example below:  

```sql
select name, namespace, uid, creationTimestamp 
from k8s.core_v1.pod 
where protocol = 'http' 
and cluster_addr = 'localhost:8080'  
order by name asc limit 3;
```
:::

### Example using direct cluster access
If you are using an access token to access the `k8s` API, follow the instructions below (use `exec` instead of `shell` for non interactive operations):

```bash
export K8S_TOKEN='eyJhbGciOiJ...'
AUTH='{ "k8s": { "type": "bearer", "credentialsenvvar": "K8S_TOKEN" } }'
stackql shell --auth="${AUTH}" --tls.CABundle k8s_cert_bundle.pem
```
:::note

You will need to generate a certificate bundle for your cluster (`k8s_cert_bundle.pem` in the preceeding example), you can use the following code to generate this (for MacOS or Linux):  

```bash
kubectl get secret -o jsonpath="{.items[?(@.type=="kubernetes.io/service-account-token")].data['ca\.crt']}" | base64 -i --decode > k8s_cert_bundle.pem
```

Alternatively, you could add the <CopyableCode code="--tls.allowInsecure=true" /> argument to the `stackql` command, it is not recommended however. 

:::


## Server Parameters


The following parameters may be required for the `k8s` provider:  

- <CopyableCode code="protocol" /> - <code>https</code> or <code>http</code> (default: <code>https</code>)
- <CopyableCode code="cluster_addr" /> - The hostname of the Kubernetes cluster (default: <code>localhost</code>)

This parameter would be supplied to the `WHERE` clause of each `SELECT` statement.
    
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/k8s/admissionregistration/">admissionregistration</a><br />
<a href="/providers/k8s/admissionregistration_v1/">admissionregistration_v1</a><br />
<a href="/providers/k8s/apiextensions/">apiextensions</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/k8s/core/">core</a><br />
<a href="/providers/k8s/core_v1/">core_v1</a><br />
</div>
</div>
