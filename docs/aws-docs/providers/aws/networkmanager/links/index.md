---
title: links
hide_title: false
hide_table_of_contents: false
keywords:
  - links
  - networkmanager
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

Creates, updates, deletes or gets a <code>link</code> resource or lists <code>links</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::Link type describes a link.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.links" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="link_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the link.</td></tr>
<tr><td><CopyableCode code="link_id" /></td><td><code>string</code></td><td>The ID of the link.</td></tr>
<tr><td><CopyableCode code="global_network_id" /></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><CopyableCode code="site_id" /></td><td><code>string</code></td><td>The ID of the site</td></tr>
<tr><td><CopyableCode code="bandwidth" /></td><td><code>object</code></td><td>The Bandwidth for the link.</td></tr>
<tr><td><CopyableCode code="provider" /></td><td><code>string</code></td><td>The provider of the link.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the link.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the link.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the link.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The date and time that the device was created.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the link.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html"><code>AWS::NetworkManager::Link</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="GlobalNetworkId, SiteId, Bandwidth, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>links</code> in a region.
```sql
SELECT
region,
link_arn,
link_id,
global_network_id,
site_id,
bandwidth,
provider,
description,
tags,
type,
created_at,
state
FROM aws.networkmanager.links
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>link</code>.
```sql
SELECT
region,
link_arn,
link_id,
global_network_id,
site_id,
bandwidth,
provider,
description,
tags,
type,
created_at,
state
FROM aws.networkmanager.links
WHERE region = 'us-east-1' AND data__Identifier = '<GlobalNetworkId>|<LinkId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>link</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.networkmanager.links (
 GlobalNetworkId,
 SiteId,
 Bandwidth,
 region
)
SELECT 
'{{ GlobalNetworkId }}',
 '{{ SiteId }}',
 '{{ Bandwidth }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.networkmanager.links (
 GlobalNetworkId,
 SiteId,
 Bandwidth,
 Provider,
 Description,
 Tags,
 Type,
 region
)
SELECT 
 '{{ GlobalNetworkId }}',
 '{{ SiteId }}',
 '{{ Bandwidth }}',
 '{{ Provider }}',
 '{{ Description }}',
 '{{ Tags }}',
 '{{ Type }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: link
    props:
      - name: GlobalNetworkId
        value: '{{ GlobalNetworkId }}'
      - name: SiteId
        value: '{{ SiteId }}'
      - name: Bandwidth
        value:
          DownloadSpeed: '{{ DownloadSpeed }}'
          UploadSpeed: '{{ UploadSpeed }}'
      - name: Provider
        value: '{{ Provider }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.networkmanager.links
WHERE data__Identifier = '<GlobalNetworkId|LinkId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>links</code> resource, the following permissions are required:

### Create
```json
networkmanager:CreateLink,
networkmanager:GetLinks,
networkmanager:TagResource
```

### Read
```json
networkmanager:GetLinks
```

### Update
```json
networkmanager:ListTagsForResource,
networkmanager:TagResource,
networkmanager:GetLinks,
networkmanager:UntagResource,
networkmanager:UpdateLink
```

### Delete
```json
networkmanager:GetLinks,
networkmanager:DeleteLink
```

### List
```json
networkmanager:GetLinks
```
