---
title: service_principal_names_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - service_principal_names_list_only
  - pcaconnectorad
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

Lists <code>service_principal_names</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/service_principal_names/"><code>service_principal_names</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_principal_names_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::PCAConnectorAD::ServicePrincipalName Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcaconnectorad.service_principal_names_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="connector_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="directory_registration_arn" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>service_principal_names</code> in a region.
```sql
SELECT
region,
connector_arn,
directory_registration_arn
FROM aws.pcaconnectorad.service_principal_names_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>service_principal_names_list_only</code> resource, see <a href="/providers/aws/pcaconnectorad/service_principal_names/#permissions"><code>service_principal_names</code></a>

