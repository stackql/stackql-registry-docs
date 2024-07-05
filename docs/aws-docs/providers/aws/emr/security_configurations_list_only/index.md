---
title: security_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - security_configurations_list_only
  - emr
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

Lists <code>security_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/security_configurations/"><code>security_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Use a SecurityConfiguration resource to configure data encryption, Kerberos authentication, and Amazon S3 authorization for EMRFS.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emr.security_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the security configuration.</td></tr>
<tr><td><CopyableCode code="security_configuration" /></td><td><code>object</code></td><td>The security configuration details in JSON format.</td></tr>
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
Lists all <code>security_configurations</code> in a region.
```sql
SELECT
region,
name
FROM aws.emr.security_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>security_configurations_list_only</code> resource, see <a href="/providers/aws/emr/security_configurations/#permissions"><code>security_configurations</code></a>


