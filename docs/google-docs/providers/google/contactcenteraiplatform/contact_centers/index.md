---
title: contact_centers
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_centers
  - contactcenteraiplatform
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

Creates, updates, deletes or gets an <code>contact_center</code> resource or lists <code>contact_centers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_centers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contactcenteraiplatform.contact_centers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | name of resource |
| <CopyableCode code="adminUser" /> | `object` | Message storing info about the first admin user. Next ID: 3 |
| <CopyableCode code="ccaipManagedUsers" /> | `boolean` | Optional. Whether to enable users to be created in the CCAIP-instance concurrently to having users in Cloud identity |
| <CopyableCode code="createTime" /> | `string` | Output only. [Output only] Create time stamp |
| <CopyableCode code="critical" /> | `object` | Instances in this Channel will receive updates after all instances in `Normal` were updated. They also will only be updated outside of their peak hours. |
| <CopyableCode code="customerDomainPrefix" /> | `string` | Required. Immutable. At least 2 and max 16 char long, must conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). |
| <CopyableCode code="displayName" /> | `string` | Required. A user friendly name for the ContactCenter. |
| <CopyableCode code="early" /> | `object` | LINT.IfChange First Channel to receive the updates. Meant to dev/test instances |
| <CopyableCode code="instanceConfig" /> | `object` | Message storing the instance configuration. |
| <CopyableCode code="kmsKey" /> | `string` | Immutable. The KMS key name to encrypt the user input (`ContactCenter`). |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs |
| <CopyableCode code="normal" /> | `object` | Instances in this Channel will receive updates after all instances in `Early` were updated + 2 days. |
| <CopyableCode code="privateAccess" /> | `object` | Defines ingress and egress private traffic settings for CCAIP instances. |
| <CopyableCode code="privateComponents" /> | `array` | Output only. TODO(b/283407860) Deprecate this field. |
| <CopyableCode code="samlParams" /> | `object` | Message storing SAML params to enable Google as IDP. |
| <CopyableCode code="state" /> | `string` | Output only. The state of this contact center. |
| <CopyableCode code="updateTime" /> | `string` | Output only. [Output only] Update time stamp |
| <CopyableCode code="uris" /> | `object` | Message storing the URIs of the ContactCenter. |
| <CopyableCode code="userEmail" /> | `string` | Optional. Email address of the first admin user. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="contactCentersId, locationsId, projectsId" /> | Gets details of a single ContactCenter. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ContactCenters in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new ContactCenter in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="contactCentersId, locationsId, projectsId" /> | Deletes a single ContactCenter. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="contactCentersId, locationsId, projectsId" /> | Updates the parameters of a single ContactCenter. |

## `SELECT` examples

Lists ContactCenters in a given project and location.

```sql
SELECT
name,
adminUser,
ccaipManagedUsers,
createTime,
critical,
customerDomainPrefix,
displayName,
early,
instanceConfig,
kmsKey,
labels,
normal,
privateAccess,
privateComponents,
samlParams,
state,
updateTime,
uris,
userEmail
FROM google.contactcenteraiplatform.contact_centers
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>contact_centers</code> resource.

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
INSERT INTO google.contactcenteraiplatform.contact_centers (
locationsId,
projectsId,
name,
createTime,
updateTime,
labels,
uris,
state,
customerDomainPrefix,
displayName,
instanceConfig,
samlParams,
userEmail,
ccaipManagedUsers,
adminUser,
kmsKey,
privateComponents,
privateAccess,
early,
normal,
critical
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ uris }}',
'{{ state }}',
'{{ customerDomainPrefix }}',
'{{ displayName }}',
'{{ instanceConfig }}',
'{{ samlParams }}',
'{{ userEmail }}',
true|false,
'{{ adminUser }}',
'{{ kmsKey }}',
'{{ privateComponents }}',
'{{ privateAccess }}',
'{{ early }}',
'{{ normal }}',
'{{ critical }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: uris
        value: '{{ uris }}'
      - name: state
        value: '{{ state }}'
      - name: customerDomainPrefix
        value: '{{ customerDomainPrefix }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: instanceConfig
        value: '{{ instanceConfig }}'
      - name: samlParams
        value: '{{ samlParams }}'
      - name: userEmail
        value: '{{ userEmail }}'
      - name: ccaipManagedUsers
        value: '{{ ccaipManagedUsers }}'
      - name: adminUser
        value: '{{ adminUser }}'
      - name: kmsKey
        value: '{{ kmsKey }}'
      - name: privateComponents
        value: '{{ privateComponents }}'
      - name: privateAccess
        value: '{{ privateAccess }}'
      - name: early
        value: '{{ early }}'
      - name: normal
        value: '{{ normal }}'
      - name: critical
        value: '{{ critical }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a contact_center only if the necessary resources are available.

```sql
UPDATE google.contactcenteraiplatform.contact_centers
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
uris = '{{ uris }}',
state = '{{ state }}',
customerDomainPrefix = '{{ customerDomainPrefix }}',
displayName = '{{ displayName }}',
instanceConfig = '{{ instanceConfig }}',
samlParams = '{{ samlParams }}',
userEmail = '{{ userEmail }}',
ccaipManagedUsers = true|false,
adminUser = '{{ adminUser }}',
kmsKey = '{{ kmsKey }}',
privateComponents = '{{ privateComponents }}',
privateAccess = '{{ privateAccess }}',
early = '{{ early }}',
normal = '{{ normal }}',
critical = '{{ critical }}'
WHERE 
contactCentersId = '{{ contactCentersId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified contact_center resource.

```sql
DELETE FROM google.contactcenteraiplatform.contact_centers
WHERE contactCentersId = '{{ contactCentersId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
