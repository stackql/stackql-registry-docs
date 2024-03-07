---
title: collaborations
hide_title: false
hide_table_of_contents: false
keywords:
  - collaborations
  - cleanrooms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>collaborations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collaborations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>collaborations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cleanrooms.collaborations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>collaboration_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>collaborations</code> resource, the following permissions are required:

### Create
```json
cleanrooms:CreateCollaboration,
cleanrooms:GetCollaboration,
cleanrooms:ListMembers,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:GetCollaboration,
cleanrooms:ListCollaborations
```

### List
```json
cleanrooms:ListCollaborations
```


## Example
```sql
SELECT
region,
collaboration_identifier
FROM awscc.cleanrooms.collaborations
WHERE region = 'us-east-1'
```
