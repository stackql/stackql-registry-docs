---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - projects
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.projects.projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `accountId` | `string` |
| `analytics` | `object` |
| `autoAssignCustomDomains` | `boolean` |
| `autoAssignCustomDomainsUpdatedBy` | `string` |
| `autoExposeSystemEnvs` | `boolean` |
| `buildCommand` | `string` |
| `commandForIgnoringBuildStep` | `string` |
| `connectBuildsEnabled` | `boolean` |
| `connectConfigurationId` | `string` |
| `createdAt` | `number` |
| `crons` | `object` |
| `customerSupportCodeVisibility` | `boolean` |
| `dataCache` | `object` |
| `devCommand` | `string` |
| `directoryListing` | `boolean` |
| `enablePreviewFeedback` | `boolean` |
| `env` | `array` |
| `framework` | `string` |
| `gitComments` | `object` |
| `gitForkProtection` | `boolean` |
| `gitLFS` | `boolean` |
| `hasActiveBranches` | `boolean` |
| `hasFloatingAliases` | `boolean` |
| `installCommand` | `string` |
| `lastAliasRequest` | `object` |
| `lastRollbackTarget` | `object` |
| `latestDeployments` | `array` |
| `link` | `` |
| `live` | `boolean` |
| `nodeVersion` | `string` |
| `outputDirectory` | `string` |
| `passwordProtection` | `object` |
| `paused` | `boolean` |
| `permissions` | `object` |
| `productionDeploymentsFastLane` | `boolean` |
| `protectionBypass` | `object` |
| `publicSource` | `boolean` |
| `rootDirectory` | `string` |
| `serverlessFunctionRegion` | `string` |
| `skipGitConnectDuringLink` | `boolean` |
| `sourceFilesOutsideRootDirectory` | `boolean` |
| `ssoProtection` | `object` |
| `targets` | `object` |
| `transferCompletedAt` | `number` |
| `transferStartedAt` | `number` |
| `transferToAccountId` | `string` |
| `transferredFromAccountId` | `string` |
| `trustedIps` | `` |
| `updatedAt` | `number` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_project` | `SELECT` | `idOrName, teamId` | Get the information for a specific project by passing either the project `id` or `name` in the URL. |
| `get_projects` | `SELECT` | `teamId` | Allows to retrieve the list of projects of the authenticated user or team. The list will be paginated and the provided query parameters allow filtering the returned projects. |
| `create_project` | `INSERT` | `teamId, data__name` | Allows to create a new project with the provided configuration. It only requires the project `name` but more configuration can be provided to override the defaults. |
| `delete_project` | `DELETE` | `idOrName, teamId` | Delete a specific project by passing either the project `id` or `name` in the URL. |
| `_get_projects` | `EXEC` | `teamId` | Allows to retrieve the list of projects of the authenticated user or team. The list will be paginated and the provided query parameters allow filtering the returned projects. |
| `update_project` | `EXEC` | `idOrName, teamId` | Update the fields of a project using either its `name` or `id`. |
| `update_project_data_cache` | `EXEC` | `projectId, teamId` | Update the data cache feature on a project. |
