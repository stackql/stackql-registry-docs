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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.projects.projects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="accountId" /> | `string` |
| <CopyableCode code="analytics" /> | `object` |
| <CopyableCode code="autoAssignCustomDomains" /> | `boolean` |
| <CopyableCode code="autoAssignCustomDomainsUpdatedBy" /> | `string` |
| <CopyableCode code="autoExposeSystemEnvs" /> | `boolean` |
| <CopyableCode code="buildCommand" /> | `string` |
| <CopyableCode code="commandForIgnoringBuildStep" /> | `string` |
| <CopyableCode code="connectBuildsEnabled" /> | `boolean` |
| <CopyableCode code="connectConfigurationId" /> | `string` |
| <CopyableCode code="createdAt" /> | `number` |
| <CopyableCode code="crons" /> | `object` |
| <CopyableCode code="customerSupportCodeVisibility" /> | `boolean` |
| <CopyableCode code="dataCache" /> | `object` |
| <CopyableCode code="devCommand" /> | `string` |
| <CopyableCode code="directoryListing" /> | `boolean` |
| <CopyableCode code="enablePreviewFeedback" /> | `boolean` |
| <CopyableCode code="env" /> | `array` |
| <CopyableCode code="framework" /> | `string` |
| <CopyableCode code="gitComments" /> | `object` |
| <CopyableCode code="gitForkProtection" /> | `boolean` |
| <CopyableCode code="gitLFS" /> | `boolean` |
| <CopyableCode code="hasActiveBranches" /> | `boolean` |
| <CopyableCode code="hasFloatingAliases" /> | `boolean` |
| <CopyableCode code="installCommand" /> | `string` |
| <CopyableCode code="lastAliasRequest" /> | `object` |
| <CopyableCode code="lastRollbackTarget" /> | `object` |
| <CopyableCode code="latestDeployments" /> | `array` |
| <CopyableCode code="link" /> ||
| <CopyableCode code="live" /> | `boolean` |
| <CopyableCode code="nodeVersion" /> | `string` |
| <CopyableCode code="outputDirectory" /> | `string` |
| <CopyableCode code="passwordProtection" /> | `object` |
| <CopyableCode code="paused" /> | `boolean` |
| <CopyableCode code="permissions" /> | `object` |
| <CopyableCode code="productionDeploymentsFastLane" /> | `boolean` |
| <CopyableCode code="protectionBypass" /> | `object` |
| <CopyableCode code="publicSource" /> | `boolean` |
| <CopyableCode code="rootDirectory" /> | `string` |
| <CopyableCode code="serverlessFunctionRegion" /> | `string` |
| <CopyableCode code="skipGitConnectDuringLink" /> | `boolean` |
| <CopyableCode code="sourceFilesOutsideRootDirectory" /> | `boolean` |
| <CopyableCode code="ssoProtection" /> | `object` |
| <CopyableCode code="targets" /> | `object` |
| <CopyableCode code="transferCompletedAt" /> | `number` |
| <CopyableCode code="transferStartedAt" /> | `number` |
| <CopyableCode code="transferToAccountId" /> | `string` |
| <CopyableCode code="transferredFromAccountId" /> | `string` |
| <CopyableCode code="trustedIps" /> ||
| <CopyableCode code="updatedAt" /> | `number` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_project" /> | `SELECT` | <CopyableCode code="idOrName, teamId" /> | Get the information for a specific project by passing either the project `id` or `name` in the URL. |
| <CopyableCode code="get_projects" /> | `SELECT` | <CopyableCode code="teamId" /> | Allows to retrieve the list of projects of the authenticated user or team. The list will be paginated and the provided query parameters allow filtering the returned projects. |
| <CopyableCode code="create_project" /> | `INSERT` | <CopyableCode code="teamId, data__name" /> | Allows to create a new project with the provided configuration. It only requires the project `name` but more configuration can be provided to override the defaults. |
| <CopyableCode code="delete_project" /> | `DELETE` | <CopyableCode code="idOrName, teamId" /> | Delete a specific project by passing either the project `id` or `name` in the URL. |
| <CopyableCode code="_get_projects" /> | `EXEC` | <CopyableCode code="teamId" /> | Allows to retrieve the list of projects of the authenticated user or team. The list will be paginated and the provided query parameters allow filtering the returned projects. |
| <CopyableCode code="update_project" /> | `EXEC` | <CopyableCode code="idOrName, teamId" /> | Update the fields of a project using either its `name` or `id`. |
| <CopyableCode code="update_project_data_cache" /> | `EXEC` | <CopyableCode code="projectId, teamId" /> | Update the data cache feature on a project. |
