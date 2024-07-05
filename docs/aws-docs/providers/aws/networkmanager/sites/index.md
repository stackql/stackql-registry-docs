---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
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

Creates, updates, deletes or gets a <code>site</code> resource or lists <code>sites</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::Site type describes a site.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.sites" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="site_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the site.</td></tr>
<tr><td><CopyableCode code="site_id" /></td><td><code>string</code></td><td>The ID of the site.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the site.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the site.</td></tr>
<tr><td><CopyableCode code="global_network_id" /></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><CopyableCode code="location" /></td><td><code>object</code></td><td>The location of the site.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The date and time that the device was created.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the site.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="GlobalNetworkId, region" /></td>
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
Gets all <code>sites</code> in a region.
```sql
SELECT
region,
site_arn,
site_id,
description,
tags,
global_network_id,
location,
created_at,
state
FROM aws.networkmanager.sites
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>site</code>.
```sql
SELECT
region,
site_arn,
site_id,
description,
tags,
global_network_id,
location,
created_at,
state
FROM aws.networkmanager.sites
WHERE region = 'us-east-1' AND data__Identifier = '<GlobalNetworkId>|<SiteId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>site</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.networkmanager.sites (
 GlobalNetworkId,
 region
)
SELECT 
'{{ GlobalNetworkId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.networkmanager.sites (
 Description,
 Tags,
 GlobalNetworkId,
 Location,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Tags }}',
 '{{ GlobalNetworkId }}',
 '{{ Location }}',
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
  - name: site
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: GlobalNetworkId
        value: '{{ GlobalNetworkId }}'
      - name: Location
        value:
          Address: '{{ Address }}'
          Latitude: '{{ Latitude }}'
          Longitude: '{{ Longitude }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.networkmanager.sites
WHERE data__Identifier = '<GlobalNetworkId|SiteId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>sites</code> resource, the following permissions are required:

### Create
```json
networkmanager:CreateSite,
networkmanager:GetSites,
networkmanager:TagResource
```

### Read
```json
networkmanager:GetSites
```

### Update
```json
networkmanager:GetSites,
networkmanager:ListTagsForResource,
networkmanager:TagResource,
networkmanager:UntagResource,
networkmanager:UpdateSite
```

### Delete
```json
networkmanager:GetSites,
networkmanager:DeleteSite
```

### List
```json
networkmanager:GetSites
```

