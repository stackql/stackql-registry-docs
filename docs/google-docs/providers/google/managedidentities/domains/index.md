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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.managedidentities.domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The unique name of the domain using the form: `projects/&#123;project_id&#125;/locations/global/domains/&#123;domain_name&#125;`. |
| <CopyableCode code="admin" /> | `string` | Optional. The name of delegated administrator account used to perform Active Directory operations. If not specified, `setupadmin` will be used. |
| <CopyableCode code="auditLogsEnabled" /> | `boolean` | Optional. Configuration for audit logs. True if audit logs are enabled, else false. Default is audit logs disabled. |
| <CopyableCode code="authorizedNetworks" /> | `array` | Optional. The full names of the Google Compute Engine [networks](/compute/docs/networks-and-firewalls#networks) the domain instance is connected to. Networks can be added using UpdateDomain. The domain is only available on networks listed in `authorized_networks`. If CIDR subnets overlap between networks, domain creation will fail. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the instance was created. |
| <CopyableCode code="fqdn" /> | `string` | Output only. The fully-qualified domain name of the exposed domain used by clients to connect to the service. Similar to what would be chosen for an Active Directory set up on an internal network. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels that can contain user-provided metadata. |
| <CopyableCode code="locations" /> | `array` | Required. Locations where domain needs to be provisioned. regions e.g. us-west1 or us-east4 Service supports up to 4 locations at once. Each location will use a /26 block. |
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
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists domains in a project. |
| <CopyableCode code="attach_trust" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Adds an AD trust to a domain. |
| <CopyableCode code="check_migration_permission" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | CheckMigrationPermission API gets the current state of DomainMigration |
| <CopyableCode code="detach_trust" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Removes an AD trust. |
| <CopyableCode code="disable_migration" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Disable Domain Migration |
| <CopyableCode code="domain_join_machine" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | DomainJoinMachine API joins a Compute Engine VM to the domain |
| <CopyableCode code="enable_migration" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Enable Domain Migration |
| <CopyableCode code="extend_schema" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Extend Schema for Domain |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Updates the metadata and configuration of a domain. |
| <CopyableCode code="reconfigure_trust" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Updates the DNS conditional forwarder. |
| <CopyableCode code="reset_admin_password" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Resets a domain's administrator password. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | RestoreDomain restores domain backup mentioned in the RestoreDomainRequest |
| <CopyableCode code="validate_trust" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests. |
