---
title: geofence_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - geofence_collections
  - location
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>geofence_collections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>geofence_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>geofence_collections</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.location.geofence_collections</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>collection_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>geofence_collections</code> resource, the following permissions are required:

### Create
```json
geo:CreateGeofenceCollection,
geo:DescribeGeofenceCollection,
geo:TagResource,
geo:UntagResource,
kms:DescribeKey,
kms:CreateGrant
```

### List
```json
geo:ListGeofenceCollections
```


## Example
```sql
SELECT
region,
collection_name
FROM awscc.location.geofence_collections
WHERE region = 'us-east-1'
```
