---
title: labs
hide_title: false
hide_table_of_contents: false
keywords:
  - labs
  - education
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>labs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>labs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.education.labs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Lab detail result properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Get the details for a specific lab associated with the provided billing account name, billing profile name, and invoice section name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Get the details for a specific lab associated with the provided billing account name, billing profile name, and invoice section name. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Get a list of labs associated with the provided billing account name and billing profile name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Create a new lab or update a previously created lab. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Delete a specific lab associated with the provided billing account name, billing profile name, and invoice section name. Note all students must be removed from the lab in order to delete the lab. |
| <CopyableCode code="generate_invite_code" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Generate invite code for a lab |

## `SELECT` examples

Get a list of labs associated with the provided billing account name and billing profile name.


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure_extras.education.labs
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>labs</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure_extras.education.labs (
billingAccountName,
billingProfileName,
invoiceSectionName,
properties
)
SELECT 
'{{ billingAccountName }}',
'{{ billingProfileName }}',
'{{ invoiceSectionName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: displayName
          value: string
        - name: budgetPerStudent
          value:
            - name: currency
              value: string
            - name: value
              value: number
        - name: description
          value: string
        - name: expirationDate
          value: string
        - name: effectiveDate
          value: string
        - name: status
          value: string
        - name: maxStudentCount
          value: number
        - name: invitationCode
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>labs</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.education.labs
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}'
AND invoiceSectionName = '{{ invoiceSectionName }}';
```
