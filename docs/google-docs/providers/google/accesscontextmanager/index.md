---
title: accesscontextmanager
hide_title: false
hide_table_of_contents: false
keywords:
  - accesscontextmanager
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

An API for setting attribute based access control to requests to Google Cloud services. *Warning:* Do not mix *v1alpha* and *v1* API usage in the same access policy. The v1alpha API supports new Access Context Manager features, which may have different attributes or behaviors that are not supported by v1. The practice of mixed API usage within a policy may result in the inability to update that policy, including any access levels or service perimeters belonging to it. It is not recommended to use both v1 and v1alpha for modifying policies with critical service perimeters. Modifications using v1alpha should be limited to policies with non-production/non-critical service perimeters.  
    
:::info Service Summary

<div class="row">
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>10</b></span><br />
<span>total selectable resources:&nbsp;<b>8</b></span><br />
<span>total methods:&nbsp;<b>47</b></span><br />
</div>
</div>

:::

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>google.accesscontextmanager</code></td></tr>
<tr><td><b>Type</b></td><td>Service</td></tr>
<tr><td><b>Title</b></td><td>Access Context Manager API</td></tr>
<tr><td><b>Description</b></td><td>An API for setting attribute based access control to requests to Google Cloud services. *Warning:* Do not mix *v1alpha* and *v1* API usage in the same access policy. The v1alpha API supports new Access Context Manager features, which may have different attributes or behaviors that are not supported by v1. The practice of mixed API usage within a policy may result in the inability to update that policy, including any access levels or service perimeters belonging to it. It is not recommended to use both v1 and v1alpha for modifying policies with critical service perimeters. Modifications using v1alpha should be limited to policies with non-production/non-critical service perimeters.</td></tr>
<tr><td><b>Id</b></td><td><code>accesscontextmanager:v24.06.00234</code></td></tr>
</tbody></table>

## Resources
<div class="row">
<div class="providerDocColumn">
<a href="/providers/google/accesscontextmanager/access_levels/">access_levels</a><br />
<a href="/providers/google/accesscontextmanager/access_levels_iam_policies/">access_levels_iam_policies</a><br />
<a href="/providers/google/accesscontextmanager/access_policies/">access_policies</a><br />
<a href="/providers/google/accesscontextmanager/access_policies_iam_policies/">access_policies_iam_policies</a><br />
<a href="/providers/google/accesscontextmanager/authorized_orgs_descs/">authorized_orgs_descs</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/google/accesscontextmanager/gcp_user_access_bindings/">gcp_user_access_bindings</a><br />
<a href="/providers/google/accesscontextmanager/operations/">operations</a><br />
<a href="/providers/google/accesscontextmanager/service_perimeters/">service_perimeters</a><br />
<a href="/providers/google/accesscontextmanager/service_perimeters_iam_policies/">service_perimeters_iam_policies</a><br />
<a href="/providers/google/accesscontextmanager/services/">services</a><br />
</div>
</div>
