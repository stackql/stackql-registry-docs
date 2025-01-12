---
title: challenges
hide_title: false
hide_table_of_contents: false
keywords:
  - challenges
  - pcaconnectorscep
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

Creates, updates, deletes or gets a <code>challenge</code> resource or lists <code>challenges</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>challenges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a SCEP Challenge that is used for certificate enrollment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcaconnectorscep.challenges" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="challenge_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="connector_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorscep-challenge.html"><code>AWS::PCAConnectorSCEP::Challenge</code></a>.

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
    <td><CopyableCode code="ConnectorArn, region" /></td>
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
Gets all <code>challenges</code> in a region.
```sql
SELECT
region,
challenge_arn,
connector_arn,
tags
FROM aws.pcaconnectorscep.challenges
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>challenge</code>.
```sql
SELECT
region,
challenge_arn,
connector_arn,
tags
FROM aws.pcaconnectorscep.challenges
WHERE region = 'us-east-1' AND data__Identifier = '<ChallengeArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>challenge</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.pcaconnectorscep.challenges (
 ConnectorArn,
 region
)
SELECT 
'{{ ConnectorArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.pcaconnectorscep.challenges (
 ConnectorArn,
 Tags,
 region
)
SELECT 
 '{{ ConnectorArn }}',
 '{{ Tags }}',
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
  - name: challenge
    props:
      - name: ConnectorArn
        value: '{{ ConnectorArn }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.pcaconnectorscep.challenges
WHERE data__Identifier = '<ChallengeArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>challenges</code> resource, the following permissions are required:

### Create
```json
pca-connector-scep:CreateChallenge,
pca-connector-scep:TagResource
```

### Read
```json
pca-connector-scep:ListTagsForResource,
pca-connector-scep:GetChallengeMetadata
```

### Delete
```json
pca-connector-scep:GetChallengeMetadata,
pca-connector-scep:DeleteChallenge,
pca-connector-scep:UntagResource
```

### List
```json
pca-connector-scep:ListChallengeMetadata
```

### Update
```json
pca-connector-scep:ListTagsForResource,
pca-connector-scep:TagResource,
pca-connector-scep:UntagResource
```