---
title: security_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - security_configurations
  - emr
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

Creates, updates, deletes or gets a <code>security_configuration</code> resource or lists <code>security_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Use a SecurityConfiguration resource to configure data encryption, Kerberos authentication, and Amazon S3 authorization for EMRFS.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emr.security_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the security configuration.</td></tr>
<tr><td><CopyableCode code="security_configuration" /></td><td><code>object</code></td><td>The security configuration details in JSON format.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html"><code>AWS::EMR::SecurityConfiguration</code></a>.

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
    <td><CopyableCode code="SecurityConfiguration, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>security_configurations</code> in a region.
```sql
SELECT
region,
name,
security_configuration
FROM aws.emr.security_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>security_configuration</code>.
```sql
SELECT
region,
name,
security_configuration
FROM aws.emr.security_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.emr.security_configurations (
 SecurityConfiguration,
 region
)
SELECT 
'{{ SecurityConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.emr.security_configurations (
 Name,
 SecurityConfiguration,
 region
)
SELECT 
 '{{ Name }}',
 '{{ SecurityConfiguration }}',
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
  - name: security_configuration
    props:
      - name: Name
        value: '{{ Name }}'
      - name: SecurityConfiguration
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.emr.security_configurations
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>security_configurations</code> resource, the following permissions are required:

### Create
```json
elasticmapreduce:CreateSecurityConfiguration,
elasticmapreduce:DescribeSecurityConfiguration
```

### Read
```json
elasticmapreduce:DescribeSecurityConfiguration
```

### Delete
```json
elasticmapreduce:DeleteSecurityConfiguration
```

### List
```json
elasticmapreduce:ListSecurityConfigurations
```
