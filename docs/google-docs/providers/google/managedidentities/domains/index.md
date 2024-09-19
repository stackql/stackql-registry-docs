---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - managedidentities
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

Creates, updates, deletes, gets or lists a <code>domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.managedidentities.domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The unique name of the domain using the form: `projects/{project_id}/locations/global/domains/{domain_name}`. |
| <CopyableCode code="admin" /> | `string` | Optional. The name of delegated administrator account used to perform Active Directory operations. If not specified, `setupadmin` will be used. |
| <CopyableCode code="auditLogsEnabled" /> | `boolean` | Optional. Configuration for audit logs. True if audit logs are enabled, else false. Default is audit logs disabled. |
| <CopyableCode code="authorizedNetworks" /> | `array` | Optional. The full names of the Google Compute Engine [networks](/compute/docs/networks-and-firewalls#networks) the domain instance is connected to. Networks can be added using UpdateDomain. The domain is only available on networks listed in `authorized_networks`. If CIDR subnets overlap between networks, domain creation will fail. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the instance was created. |
| <CopyableCode code="fqdn" /> | `string` | Output only. The fully-qualified domain name of the exposed domain used by clients to connect to the service. Similar to what would be chosen for an Active Directory set up on an internal network. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels that can contain user-provided metadata. |
| <CopyableCode code="locations" /> | `array` | Required. Locations where domain needs to be provisioned. The locations can be specified according to https://cloud.google.com/compute/docs/regions-zones, such as `us-west1` or `us-east4`. Each domain supports up to 4 locations, separated by commas. Each location will use a /26 block. |
| <CopyableCode code="reservedIpRange" /> | `string` | Required. The CIDR range of internal addresses that are reserved for this domain. Reserved networks must be /24 or larger. Ranges must be unique and non-overlapping with existing subnets in [Domain].[authorized_networks]. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of this domain. |
| <CopyableCode code="statusMessage" /> | `string` | Output only. Additional information about the current status of this domain, if available. |
| <CopyableCode code="trusts" /> | `array` | Output only. The current trusts associated with the domain. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainsId, projectsId" /> | Gets information about a domain. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists domains in a project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a Microsoft AD domain. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainsId, projectsId" /> | Deletes a domain. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="domainsId, projectsId" /> | Updates the metadata and configuration of a domain. |
| <CopyableCode code="attach_trust" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Adds an AD trust to a domain. |
| <CopyableCode code="check_migration_permission" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | CheckMigrationPermission API gets the current state of DomainMigration |
| <CopyableCode code="detach_trust" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Removes an AD trust. |
| <CopyableCode code="disable_migration" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Disable Domain Migration |
| <CopyableCode code="domain_join_machine" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | DomainJoinMachine API joins a Compute Engine VM to the domain |
| <CopyableCode code="enable_migration" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Enable Domain Migration |
| <CopyableCode code="extend_schema" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Extend Schema for Domain |
| <CopyableCode code="reconfigure_trust" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Updates the DNS conditional forwarder. |
| <CopyableCode code="reset_admin_password" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Resets a domain's administrator password. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | RestoreDomain restores domain backup mentioned in the RestoreDomainRequest |
| <CopyableCode code="validate_trust" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests. |

## `SELECT` examples

Lists domains in a project.

```sql
SELECT
name,
admin,
auditLogsEnabled,
authorizedNetworks,
createTime,
fqdn,
labels,
locations,
reservedIpRange,
state,
statusMessage,
trusts,
updateTime
FROM google.managedidentities.domains
WHERE projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domains</code> resource.

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
INSERT INTO google.managedidentities.domains (
projectsId,
name,
labels,
authorizedNetworks,
reservedIpRange,
locations,
admin,
auditLogsEnabled
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ labels }}',
'{{ authorizedNetworks }}',
'{{ reservedIpRange }}',
'{{ locations }}',
'{{ admin }}',
{{ auditLogsEnabled }}
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: labels
      value: object
    - name: authorizedNetworks
      value:
        - string
    - name: reservedIpRange
      value: string
    - name: locations
      value:
        - string
    - name: admin
      value: string
    - name: fqdn
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: state
      value: string
    - name: statusMessage
      value: string
    - name: trusts
      value:
        - - name: targetDomainName
            value: string
          - name: trustType
            value: string
          - name: trustDirection
            value: string
          - name: selectiveAuthentication
            value: boolean
          - name: targetDnsIpAddresses
            value:
              - string
          - name: trustHandshakeSecret
            value: string
          - name: createTime
            value: string
          - name: updateTime
            value: string
          - name: state
            value: string
          - name: stateDescription
            value: string
          - name: lastTrustHeartbeatTime
            value: string
    - name: auditLogsEnabled
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>domains</code> resource.

```sql
/*+ update */
UPDATE google.managedidentities.domains
SET 
name = '{{ name }}',
labels = '{{ labels }}',
authorizedNetworks = '{{ authorizedNetworks }}',
reservedIpRange = '{{ reservedIpRange }}',
locations = '{{ locations }}',
admin = '{{ admin }}',
auditLogsEnabled = true|false
WHERE 
domainsId = '{{ domainsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>domains</code> resource.

```sql
/*+ delete */
DELETE FROM google.managedidentities.domains
WHERE domainsId = '{{ domainsId }}'
AND projectsId = '{{ projectsId }}';
```
