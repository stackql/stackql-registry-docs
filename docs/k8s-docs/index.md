---
title: k8s
hide_title: false
hide_table_of_contents: false
keywords:
  - kubernetes
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
Open source container management platform.  

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;&nbsp;&nbsp;<b>5</b></span><br />
<span>total methods:&nbsp;<b>267</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>33</b></span><br />
<span>total selectable resources:&nbsp;<b>24</b></span><br />
</div>
</div>

:::

## Installation
```bash
REGISTRY PULL k8s v23.01.00104;
```

## Authentication
```javascript
{
  "k8s": {
    /**
      * Type of authentication to use, suported values include: api_key, null_auth
      * @type String
      */
    "type": string, 
    /**
      * Environment variable name containing the api key or credentials.
      * @type String
      */
    "credentialsenvvar": string, 
    /**
      * Value prepended to the request header, e.g. "Bearer "
      * Must be set to "Bearer "
      * @type String
      */
    "valuePrefix": string, 
  }
}
```

:::note

__`cluster_addr`__ is a required paramter for all operations using the `k8s` provider, for example:  

```sql
SELECT name, namespace, uid, creationTimestamp 
FROM k8s.core_v1.service_account 
WHERE cluster_addr = '35.244.65.136' AND namespace = 'kube-system' 
ORDER BY name ASC;
```
:::

### Example using `kubectl proxy`
```bash
AUTH='{ "k8s": { "type": "null_auth" } }'
./stackql shell --auth="${AUTH}"
```

:::note

The __`protocol`__ parameter is required when accessing a Kubernetes cluster via `kubectl proxy`, see the example below:  

```sql
select name, namespace, uid, creationTimestamp 
from k8s.core_v1.pod 
where protocol = 'http' 
and cluster_addr = 'localhost:8080'  
order by name asc limit 3;
```
:::

### Example using direct cluster access
```bash
export K8S_TOKEN='eyJhbGciOiJ...'
AUTH='{ "k8s": { "type": "api_key", "valuePrefix": "Bearer ", "credentialsenvvar": "K8S_TOKEN" } }'
stackql shell --auth="${AUTH}" --tls.CABundle k8s_cert_bundle.pem
```
:::note

You will need to generate a certificate bundle for your cluster (`k8s_cert_bundle.pem` in the preceeding example), you can use the following code to generate this (for MacOS or Linux):  

```bash
kubectl get secret -o jsonpath="{.items[?(@.type==\"kubernetes.io/service-account-token\")].data['ca\.crt']}" | base64 -i --decode > k8s_cert_bundle.pem
```

Alternatively, you could add the `--tls.allowInsecure=true` argument to the `stackql` command, it is not recommended however. 

:::

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/k8s/core/">core</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/k8s/core_v1/">core_v1</a><br />
</div>
</div>
