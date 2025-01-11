---
title: invoice_units
hide_title: false
hide_table_of_contents: false
keywords:
  - invoice_units
  - invoicing
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

Creates, updates, deletes or gets an <code>invoice_unit</code> resource or lists <code>invoice_units</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invoice_units</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An invoice unit is a set of mutually exclusive accounts that correspond to your business entity. Invoice units allow you to separate AWS account costs and configures your invoice for each business entity.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.invoicing.invoice_units" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="invoice_unit_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="invoice_receiver" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tax_inheritance_disabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="rule" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modified" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html"><code>AWS::Invoicing::InvoiceUnit</code></a>.

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
    <td><CopyableCode code="InvoiceReceiver, Name, Rule, region" /></td>
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
Gets all <code>invoice_units</code> in a region.
```sql
SELECT
region,
invoice_unit_arn,
invoice_receiver,
name,
description,
tax_inheritance_disabled,
rule,
last_modified,
resource_tags
FROM aws.invoicing.invoice_units
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>invoice_unit</code>.
```sql
SELECT
region,
invoice_unit_arn,
invoice_receiver,
name,
description,
tax_inheritance_disabled,
rule,
last_modified,
resource_tags
FROM aws.invoicing.invoice_units
WHERE region = 'us-east-1' AND data__Identifier = '<InvoiceUnitArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>invoice_unit</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.invoicing.invoice_units (
 InvoiceReceiver,
 Name,
 Rule,
 region
)
SELECT 
'{{ InvoiceReceiver }}',
 '{{ Name }}',
 '{{ Rule }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.invoicing.invoice_units (
 InvoiceReceiver,
 Name,
 Description,
 TaxInheritanceDisabled,
 Rule,
 ResourceTags,
 region
)
SELECT 
 '{{ InvoiceReceiver }}',
 '{{ Name }}',
 '{{ Description }}',
 '{{ TaxInheritanceDisabled }}',
 '{{ Rule }}',
 '{{ ResourceTags }}',
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
  - name: invoice_unit
    props:
      - name: InvoiceReceiver
        value: '{{ InvoiceReceiver }}'
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: TaxInheritanceDisabled
        value: '{{ TaxInheritanceDisabled }}'
      - name: Rule
        value:
          LinkedAccounts:
            - '{{ LinkedAccounts[0] }}'
      - name: ResourceTags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.invoicing.invoice_units
WHERE data__Identifier = '<InvoiceUnitArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>invoice_units</code> resource, the following permissions are required:

### Create
```json
invoicing:CreateInvoiceUnit,
invoicing:TagResource
```

### Read
```json
invoicing:GetInvoiceUnit,
invoicing:ListTagsForResource
```

### Update
```json
invoicing:UpdateInvoiceUnit,
invoicing:UntagResource,
invoicing:TagResource
```

### Delete
```json
invoicing:DeleteInvoiceUnit
```

### List
```json
invoicing:ListInvoiceUnits
```
