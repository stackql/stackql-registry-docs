---
title: domain_name_access_association_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_name_access_association_tags
  - apigateway
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

Expands all tag keys and values for <code>domain_name_access_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_name_access_association_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ApiGateway::DomainNameAccessAssociation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.domain_name_access_association_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name_access_association_arn" /></td><td><code>string</code></td><td>The amazon resource name (ARN) of the domain name access association resource.</td></tr>
<tr><td><CopyableCode code="domain_name_arn" /></td><td><code>string</code></td><td>The amazon resource name (ARN) of the domain name resource.</td></tr>
<tr><td><CopyableCode code="access_association_source" /></td><td><code>string</code></td><td>The source of the domain name access association resource.</td></tr>
<tr><td><CopyableCode code="access_association_source_type" /></td><td><code>string</code></td><td>The source type of the domain name access association resource.</td></tr>
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
Expands tags for all <code>domain_name_access_associations</code> in a region.
```sql
SELECT
region,
domain_name_access_association_arn,
domain_name_arn,
access_association_source,
access_association_source_type,
tag_key,
tag_value
FROM aws.apigateway.domain_name_access_association_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>domain_name_access_association_tags</code> resource, see <a href="/providers/aws/apigateway/domain_name_access_associations/#permissions"><code>domain_name_access_associations</code></a>

