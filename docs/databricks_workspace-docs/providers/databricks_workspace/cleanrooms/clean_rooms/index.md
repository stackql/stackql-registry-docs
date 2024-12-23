---
title: clean_rooms
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - clean_rooms
  - cleanrooms
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>clean_rooms</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clean_rooms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.cleanrooms.clean_rooms" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="access_restricted" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="local_collaborator_alias" /> | `string` |
| <CopyableCode code="output_catalog" /> | `object` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="remote_detailed_info" /> | `object` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Get the details of a clean room given its name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Get a list of all clean rooms of the metastore. Only clean rooms the caller has access to are returned. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Create a new clean room with the specified collaborators. This method is asynchronous; the returned name field inside the clean_room field can be used to poll the clean room status, using the |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, deployment_name" /> | Delete a clean room. After deletion, the clean room will be removed from the metastore. If the other collaborators have not deleted the clean room, they will still have the clean room in their metastore, but it will be in a DELETED state and no operations other than deletion can be performed on it. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Update a clean room. The caller must be the owner of the clean room, have |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'clean_rooms (list)', value: 'list' },
        { label: 'clean_rooms (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
name,
access_restricted,
comment,
created_at,
local_collaborator_alias,
output_catalog,
owner,
remote_detailed_info,
status,
updated_at
FROM databricks_workspace.cleanrooms.clean_rooms
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
access_restricted,
comment,
created_at,
local_collaborator_alias,
output_catalog,
owner,
remote_detailed_info,
status,
updated_at
FROM databricks_workspace.cleanrooms.clean_rooms
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clean_rooms</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'clean_rooms', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.cleanrooms.clean_rooms (
deployment_name,
data__name,
data__remote_detailed_info,
data__owner,
data__comment
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ remote_detailed_info }}',
'{{ owner }}',
'{{ comment }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: test-clean-room1
  - name: remote_detailed_info
    value:
      central_clean_room_id: b5c8d856-ff41-4c5f-8ccd-2b13b44fec27
      cloud_vendor: aws
      region: us-west-2
      collaborators:
      - global_metastore_id: aws:us-west-2:aff56c64-a34e-4c1f-a24c-c2dd2889517a
        organization_name: acme corporation
        invite_recipient_workspace_id: 6822898386300992
        invite_recipient_email: john.doe@databricks.com
        collaborator_alias: creator
        display_name: acme corporation
      creator:
        global_metastore_id: aws:us-west-2:aff56c64-a34e-4c1f-a24c-c2dd2889517a
        organization_name: acme corporation
        invite_recipient_workspace_id: 6822898386300992
        invite_recipient_email: john.doe@databricks.com
        collaborator_alias: creator
        display_name: acme corporation
      egress_network_policy:
        internet_access:
          restriction_mode: FULL_ACCESS
          allowed_internet_destinations:
          - destination: string
            type: FQDN
            protocol: TCP
          allowed_storage_destinations:
          - bucket_name: string
            region: string
            type: AWS_S3
            azure_storage_account: string
            allowed_paths:
            - string
            azure_storage_service: string
            azure_dns_zone: string
            azure_container: string
          log_only_mode:
            log_only_mode_type: ALL_SERVICES
            workloads:
            - DBSQL
      compliance_security_profile:
        is_enabled: true
        compliance_standards:
        - NONE
  - name: owner
    value: alice@example.com
  - name: comment
    value: This is a clean room for demo

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>clean_rooms</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.cleanrooms.clean_rooms
SET { field = value }
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>clean_rooms</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.cleanrooms.clean_rooms
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
