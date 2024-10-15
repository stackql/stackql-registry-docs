---
title: students
hide_title: false
hide_table_of_contents: false
keywords:
  - students
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

Creates, updates, deletes, gets or lists a <code>students</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>students</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.education.students" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_students', value: 'view', },
        { label: 'students', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="budget" /> | `text` | field from the `properties` object |
| <CopyableCode code="effective_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="email" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="first_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoiceSectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="role" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="studentAlias" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_alias" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_invite_last_sent_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Student detail properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName, studentAlias" /> | Get the details for a specific student in the specified lab by student alias |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Get a list of details about students that are associated with the specified lab. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName, studentAlias" /> | Create and add a new student to the specified lab or update the details of an existing student in a lab. Note the student must have a valid tenant to accept the lab after they have been added to lab. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName, studentAlias" /> | Delete the specified student based on the student alias. |

## `SELECT` examples

Get a list of details about students that are associated with the specified lab.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_students', value: 'view', },
        { label: 'students', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
billingAccountName,
billingProfileName,
budget,
effective_date,
email,
expiration_date,
first_name,
invoiceSectionName,
last_name,
role,
status,
studentAlias,
subscription_alias,
subscription_id,
subscription_invite_last_sent_date,
system_data,
type
FROM azure_extras.education.vw_students
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}'
AND invoiceSectionName = '{{ invoiceSectionName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure_extras.education.students
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}'
AND invoiceSectionName = '{{ invoiceSectionName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>students</code> resource.

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
INSERT INTO azure_extras.education.students (
billingAccountName,
billingProfileName,
invoiceSectionName,
studentAlias,
properties
)
SELECT 
'{{ billingAccountName }}',
'{{ billingProfileName }}',
'{{ invoiceSectionName }}',
'{{ studentAlias }}',
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
        - name: firstName
          value: string
        - name: lastName
          value: string
        - name: email
          value: string
        - name: role
          value: string
        - name: budget
          value:
            - name: currency
              value: string
            - name: value
              value: number
        - name: subscriptionId
          value: string
        - name: expirationDate
          value: string
        - name: status
          value: string
        - name: effectiveDate
          value: string
        - name: subscriptionAlias
          value: string
        - name: subscriptionInviteLastSentDate
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>students</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.education.students
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}'
AND invoiceSectionName = '{{ invoiceSectionName }}'
AND studentAlias = '{{ studentAlias }}';
```
