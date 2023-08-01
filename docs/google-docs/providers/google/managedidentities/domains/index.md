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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.managedidentities.domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `domains` | `array` | A list of Managed Identities Service domains in the project. |
| `nextPageToken` | `string` | A token to retrieve the next page of results, or empty if there are no more results in the list. |
| `unreachable` | `array` | A list of locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `domainsId, projectsId` | Gets information about a domain. |
| `list` | `SELECT` | `projectsId` | Lists domains in a project. |
| `create` | `INSERT` | `projectsId` | Creates a Microsoft AD domain. |
| `delete` | `DELETE` | `domainsId, projectsId` | Deletes a domain. |
| `attach_trust` | `EXEC` | `domainsId, projectsId` | Adds an AD trust to a domain. |
| `check_migration_permission` | `EXEC` | `domainsId, projectsId` | CheckMigrationPermission API gets the current state of DomainMigration |
| `detach_trust` | `EXEC` | `domainsId, projectsId` | Removes an AD trust. |
| `disable_migration` | `EXEC` | `domainsId, projectsId` | Disable Domain Migration |
| `domain_join_machine` | `EXEC` | `domainsId, projectsId` | DomainJoinMachine API joins a Compute Engine VM to the domain |
| `enable_migration` | `EXEC` | `domainsId, projectsId` | Enable Domain Migration |
| `extend_schema` | `EXEC` | `domainsId, projectsId` | Extend Schema for Domain |
| `patch` | `EXEC` | `domainsId, projectsId` | Updates the metadata and configuration of a domain. |
| `reconfigure_trust` | `EXEC` | `domainsId, projectsId` | Updates the DNS conditional forwarder. |
| `reset_admin_password` | `EXEC` | `domainsId, projectsId` | Resets a domain's administrator password. |
| `restore` | `EXEC` | `domainsId, projectsId` | RestoreDomain restores domain backup mentioned in the RestoreDomainRequest |
| `validate_trust` | `EXEC` | `domainsId, projectsId` | Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests. |
