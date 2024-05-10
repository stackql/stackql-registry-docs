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


Used to retrieve a list of <code>sites</code> in a region or to create or delete a <code>sites</code> resource, use <code>site</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::Site type describes a site.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.sites" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="global_network_id" /></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><CopyableCode code="site_id" /></td><td><code>string</code></td><td>The ID of the site.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
global_network_id,
site_id
FROM aws.networkmanager.sites
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "GlobalNetworkId": "{{ GlobalNetworkId }}"
}
>>>
--required properties only
INSERT INTO aws.networkmanager.sites (
 GlobalNetworkId,
 region
)
SELECT 
{{ GlobalNetworkId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "GlobalNetworkId": "{{ GlobalNetworkId }}",
 "Location": {
  "Address": "{{ Address }}",
  "Latitude": "{{ Latitude }}",
  "Longitude": "{{ Longitude }}"
 }
}
>>>
--all properties
INSERT INTO aws.networkmanager.sites (
 Description,
 Tags,
 GlobalNetworkId,
 Location,
 region
)
SELECT 
 {{ Description }},
 {{ Tags }},
 {{ GlobalNetworkId }},
 {{ Location }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
networkmanager:GetSites,
networkmanager:DeleteSite
```

### List
```json
networkmanager:GetSites
```

