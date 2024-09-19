---
title: gcp_user_access_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - gcp_user_access_bindings
  - accesscontextmanager
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

Creates, updates, deletes, gets or lists a <code>gcp_user_access_bindings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gcp_user_access_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.accesscontextmanager.gcp_user_access_bindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Assigned by the server during creation. The last segment has an arbitrary length and has only URI unreserved characters (as defined by [RFC 3986 Section 2.3](https://tools.ietf.org/html/rfc3986#section-2.3)). Should not be specified by the client during creation. Example: "organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N" |
| <CopyableCode code="accessLevels" /> | `array` | Optional. Access level that a user must have to be granted access. Only one access level is supported, not multiple. This repeated field must have exactly one element. Example: "accessPolicies/9522/accessLevels/device_trusted" |
| <CopyableCode code="dryRunAccessLevels" /> | `array` | Optional. Dry run access level that will be evaluated but will not be enforced. The access denial based on dry run policy will be logged. Only one access level is supported, not multiple. This list must have exactly one element. Example: "accessPolicies/9522/accessLevels/device_trusted" |
| <CopyableCode code="groupKey" /> | `string` | Required. Immutable. Google Group id whose members are subject to this binding's restrictions. See "id" in the [G Suite Directory API's Groups resource] (https://developers.google.com/admin-sdk/directory/v1/reference/groups#resource). If a group's email address/alias is changed, this resource will continue to point at the changed group. This field does not accept group email addresses or aliases. Example: "01d520gv4vjcrht" |
| <CopyableCode code="reauthSettings" /> | `object` | Stores settings related to Google Cloud Session Length including session duration, the type of challenge (i.e. method) they should face when their session expires, and other related settings. |
| <CopyableCode code="restrictedClientApplications" /> | `array` | Optional. A list of applications that are subject to this binding's restrictions. If the list is empty, the binding restrictions will universally apply to all applications. |
| <CopyableCode code="scopedAccessSettings" /> | `array` | Optional. A list of scoped access settings that set this binding's restrictions on a subset of applications. This field cannot be set if restricted_client_applications is set. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gcpUserAccessBindingsId, organizationsId" /> | Gets the GcpUserAccessBinding with the given name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all GcpUserAccessBindings for a Google Cloud organization. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a GcpUserAccessBinding. If the client specifies a name, the server ignores it. Fails if a resource already exists with the same group_key. Completion of this long-running operation does not necessarily signify that the new binding is deployed onto all affected users, which may take more time. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="gcpUserAccessBindingsId, organizationsId" /> | Deletes a GcpUserAccessBinding. Completion of this long-running operation does not necessarily signify that the binding deletion is deployed onto all affected users, which may take more time. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="gcpUserAccessBindingsId, organizationsId" /> | Updates a GcpUserAccessBinding. Completion of this long-running operation does not necessarily signify that the changed binding is deployed onto all affected users, which may take more time. |

## `SELECT` examples

Lists all GcpUserAccessBindings for a Google Cloud organization.

```sql
SELECT
name,
accessLevels,
dryRunAccessLevels,
groupKey,
reauthSettings,
restrictedClientApplications,
scopedAccessSettings
FROM google.accesscontextmanager.gcp_user_access_bindings
WHERE organizationsId = '{{ organizationsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gcp_user_access_bindings</code> resource.

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
INSERT INTO google.accesscontextmanager.gcp_user_access_bindings (
organizationsId,
name,
groupKey,
accessLevels,
dryRunAccessLevels,
reauthSettings,
restrictedClientApplications,
scopedAccessSettings
)
SELECT 
'{{ organizationsId }}',
'{{ name }}',
'{{ groupKey }}',
'{{ accessLevels }}',
'{{ dryRunAccessLevels }}',
'{{ reauthSettings }}',
'{{ restrictedClientApplications }}',
'{{ scopedAccessSettings }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: groupKey
      value: string
    - name: accessLevels
      value:
        - string
    - name: dryRunAccessLevels
      value:
        - string
    - name: reauthSettings
      value:
        - name: reauthMethod
          value: string
        - name: sessionLength
          value: string
        - name: maxInactivity
          value: string
        - name: useOidcMaxAge
          value: boolean
        - name: sessionLengthEnabled
          value: boolean
    - name: restrictedClientApplications
      value:
        - - name: clientId
            value: string
          - name: name
            value: string
    - name: scopedAccessSettings
      value:
        - - name: scope
            value:
              - name: clientScope
                value:
                  - name: restrictedClientApplication
                    value:
                      - name: clientId
                        value: string
                      - name: name
                        value: string
          - name: activeSettings
            value:
              - name: accessLevels
                value:
                  - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>gcp_user_access_bindings</code> resource.

```sql
/*+ update */
UPDATE google.accesscontextmanager.gcp_user_access_bindings
SET 
name = '{{ name }}',
groupKey = '{{ groupKey }}',
accessLevels = '{{ accessLevels }}',
dryRunAccessLevels = '{{ dryRunAccessLevels }}',
reauthSettings = '{{ reauthSettings }}',
restrictedClientApplications = '{{ restrictedClientApplications }}',
scopedAccessSettings = '{{ scopedAccessSettings }}'
WHERE 
gcpUserAccessBindingsId = '{{ gcpUserAccessBindingsId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `DELETE` example

Deletes the specified <code>gcp_user_access_bindings</code> resource.

```sql
/*+ delete */
DELETE FROM google.accesscontextmanager.gcp_user_access_bindings
WHERE gcpUserAccessBindingsId = '{{ gcpUserAccessBindingsId }}'
AND organizationsId = '{{ organizationsId }}';
```
