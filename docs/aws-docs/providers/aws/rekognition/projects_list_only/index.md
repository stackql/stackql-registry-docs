---
title: projects_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - projects_list_only
  - rekognition
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

Lists <code>projects</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/projects/"><code>projects</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Rekognition::Project type creates an Amazon Rekognition CustomLabels Project. A project is a grouping of the resources needed to create and manage Dataset and ProjectVersions.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rekognition.projects_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="project_name" /></td><td><code>string</code></td><td>The name of the project</td></tr>
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
Lists all <code>projects</code> in a region.
```sql
SELECT
region,
project_name
FROM aws.rekognition.projects_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>projects_list_only</code> resource, see <a href="/providers/aws/rekognition/projects/#permissions"><code>projects</code></a>

