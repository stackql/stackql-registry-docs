---
title: studios_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - studios_list_only
  - nimblestudio
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

Lists <code>studios</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/studios/"><code>studios</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studios_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a studio that contains other Nimble Studio resources</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.studios_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="admin_role_arn" /></td><td><code>string</code></td><td><p>The IAM role that Studio Admins will assume when logging in to the Nimble Studio portal.</p></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td><p>A friendly name for the studio.</p></td></tr>
<tr><td><CopyableCode code="home_region" /></td><td><code>string</code></td><td><p>The Amazon Web Services Region where the studio resource is located.</p></td></tr>
<tr><td><CopyableCode code="sso_client_id" /></td><td><code>string</code></td><td><p>The Amazon Web Services SSO application client ID used to integrate with Amazon Web Services SSO to enable Amazon Web Services SSO users to log in to Nimble Studio portal.</p></td></tr>
<tr><td><CopyableCode code="studio_encryption_configuration" /></td><td><code>object</code></td><td><p>Configuration of the encryption method that is used for the studio.</p></td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_name" /></td><td><code>string</code></td><td><p>The studio name that is used in the URL of the Nimble Studio portal when accessed by Nimble Studio users.</p></td></tr>
<tr><td><CopyableCode code="studio_url" /></td><td><code>string</code></td><td><p>The address of the web page for the studio.</p></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="user_role_arn" /></td><td><code>string</code></td><td><p>The IAM role that Studio Users will assume when logging in to the Nimble Studio portal.</p></td></tr>
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
Lists all <code>studios</code> in a region.
```sql
SELECT
region,
studio_id
FROM aws.nimblestudio.studios_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>studios_list_only</code> resource, see <a href="/providers/aws/nimblestudio/studios/#permissions"><code>studios</code></a>


