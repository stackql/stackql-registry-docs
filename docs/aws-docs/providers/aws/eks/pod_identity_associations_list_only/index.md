---
title: pod_identity_associations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - pod_identity_associations_list_only
  - eks
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>pod_identity_associations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/pod_identity_associations/"><code>pod_identity_associations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pod_identity_associations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS PodIdentityAssociation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.pod_identity_associations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="association_arn" /></td><td><code>string</code></td><td>The ARN of the pod identity association.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>pod_identity_associations</code> in a region.
```sql
SELECT
region,
association_arn
FROM aws.eks.pod_identity_associations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>pod_identity_associations_list_only</code> resource, see <a href="/providers/aws/eks/pod_identity_associations/#permissions"><code>pod_identity_associations</code></a>

