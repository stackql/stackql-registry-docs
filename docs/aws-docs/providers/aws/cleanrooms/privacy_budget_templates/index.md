---
title: privacy_budget_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - privacy_budget_templates
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>privacy_budget_templates</code> in a region or to create or delete a <code>privacy_budget_templates</code> resource, use <code>privacy_budget_template</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>privacy_budget_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a privacy budget within a collaboration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.privacy_budget_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="privacy_budget_template_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="membership_identifier" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="AutoRefresh, PrivacyBudgetType, Parameters, MembershipIdentifier, region" /></td>
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
privacy_budget_template_identifier,
membership_identifier
FROM aws.cleanrooms.privacy_budget_templates
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>privacy_budget_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cleanrooms.privacy_budget_templates (
 AutoRefresh,
 PrivacyBudgetType,
 Parameters,
 MembershipIdentifier,
 region
)
SELECT 
'{{ AutoRefresh }}',
 '{{ PrivacyBudgetType }}',
 '{{ Parameters }}',
 '{{ MembershipIdentifier }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cleanrooms.privacy_budget_templates (
 Tags,
 AutoRefresh,
 PrivacyBudgetType,
 Parameters,
 MembershipIdentifier,
 region
)
SELECT 
 '{{ Tags }}',
 '{{ AutoRefresh }}',
 '{{ PrivacyBudgetType }}',
 '{{ Parameters }}',
 '{{ MembershipIdentifier }}',
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
  - name: privacy_budget_template
    props:
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AutoRefresh
        value: '{{ AutoRefresh }}'
      - name: PrivacyBudgetType
        value: '{{ PrivacyBudgetType }}'
      - name: Parameters
        value:
          Epsilon: '{{ Epsilon }}'
          UsersNoisePerQuery: '{{ UsersNoisePerQuery }}'
      - name: MembershipIdentifier
        value: '{{ MembershipIdentifier }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.cleanrooms.privacy_budget_templates
WHERE data__Identifier = '<PrivacyBudgetTemplateIdentifier|MembershipIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>privacy_budget_templates</code> resource, the following permissions are required:

### Create
```json
cleanrooms:CreatePrivacyBudgetTemplate,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:GetPrivacyBudgetTemplate,
cleanrooms:ListPrivacyBudgetTemplates
```

### Delete
```json
cleanrooms:DeletePrivacyBudgetTemplate,
cleanrooms:GetPrivacyBudgetTemplate,
cleanrooms:ListPrivacyBudgetTemplates,
cleanrooms:ListTagsForResource,
cleanrooms:UntagResource
```

### List
```json
cleanrooms:ListPrivacyBudgetTemplates
```

