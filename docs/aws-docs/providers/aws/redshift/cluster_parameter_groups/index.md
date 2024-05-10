---
title: cluster_parameter_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_parameter_groups
  - redshift
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


Used to retrieve a list of <code>cluster_parameter_groups</code> in a region or to create or delete a <code>cluster_parameter_groups</code> resource, use <code>cluster_parameter_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_parameter_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Redshift::ClusterParameterGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.cluster_parameter_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="parameter_group_name" /></td><td><code>string</code></td><td>The name of the cluster parameter group.</td></tr>
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
parameter_group_name
FROM aws.redshift.cluster_parameter_groups
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
 "Description": "{{ Description }}",
 "ParameterGroupFamily": "{{ ParameterGroupFamily }}"
}
>>>
--required properties only
INSERT INTO aws.redshift.cluster_parameter_groups (
 Description,
 ParameterGroupFamily,
 region
)
SELECT 
{{ Description }},
 {{ ParameterGroupFamily }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ParameterGroupName": "{{ ParameterGroupName }}",
 "Description": "{{ Description }}",
 "ParameterGroupFamily": "{{ ParameterGroupFamily }}",
 "Parameters": [
  {
   "ParameterName": "{{ ParameterName }}",
   "ParameterValue": "{{ ParameterValue }}"
  }
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.redshift.cluster_parameter_groups (
 ParameterGroupName,
 Description,
 ParameterGroupFamily,
 Parameters,
 Tags,
 region
)
SELECT 
 {{ ParameterGroupName }},
 {{ Description }},
 {{ ParameterGroupFamily }},
 {{ Parameters }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.redshift.cluster_parameter_groups
WHERE data__Identifier = '<ParameterGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>cluster_parameter_groups</code> resource, the following permissions are required:

### Create
```json
redshift:CreateClusterParameterGroup,
redshift:ModifyClusterParameterGroup,
redshift:DescribeClusterParameterGroups,
redshift:DescribeClusterParameters,
redshift:DescribeTags,
redshift:CreateTags,
ec2:AllocateAddress,
ec2:AssociateAddress,
ec2:AttachNetworkInterface,
ec2:DescribeAccountAttributes,
ec2:DescribeAddresses,
ec2:DescribeAvailabilityZones,
ec2:DescribeInternetGateways,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcs
```

### Delete
```json
redshift:DescribeTags,
redshift:DescribeClusterParameterGroups,
redshift:DeleteClusterParameterGroup,
redshift:DescribeClusterParameters,
initech:DeleteReport
```

### List
```json
redshift:DescribeTags,
redshift:DescribeClusterParameterGroups,
redshift:DescribeClusterParameters,
initech:ListReports
```

