---
title: application_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - application_tags
  - appintegrations
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

Expands all tag keys and values for <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS:AppIntegrations::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appintegrations.application_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the application.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The id of the application.</td></tr>
<tr><td><CopyableCode code="namespace" /></td><td><code>string</code></td><td>The namespace of the application.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The application description.</td></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the application.</td></tr>
<tr><td><CopyableCode code="application_source_config" /></td><td><code>object</code></td><td>Application source config</td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td>The configuration of events or requests that the application has access to.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>applications</code> in a region.
```sql
SELECT
region,
name,
id,
namespace,
description,
application_arn,
application_source_config,
permissions,
tag_key,
tag_value
FROM aws.appintegrations.application_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>application_tags</code> resource, see <a href="/providers/aws/appintegrations/applications/#permissions"><code>applications</code></a>

