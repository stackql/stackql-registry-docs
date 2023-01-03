---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - appengine
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.appengine.versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Relative name of the version within the service. Example: v1. Version names can contain only lowercase letters, numbers, or hyphens. Reserved names: "default", "latest", and any name with the prefix "ah-". |
| `name` | `string` | Full path to the Version resource in the API. Example: apps/myapp/services/default/versions/v1.@OutputOnly |
| `runtimeChannel` | `string` | The channel of the runtime to use. Only available for some runtimes. Defaults to the default channel. |
| `libraries` | `array` | Configuration for third-party Python runtime libraries that are required by the application.Only returned in GET requests if view=FULL is set. |
| `envVariables` | `object` | Environment variables available to the application.Only returned in GET requests if view=FULL is set. |
| `endpointsApiService` | `object` | Cloud Endpoints (https://cloud.google.com/endpoints) configuration. The Endpoints API Service provides tooling for serving Open API and gRPC endpoints via an NGINX proxy. Only valid for App Engine Flexible environment deployments.The fields here refer to the name and configuration ID of a "service" resource in the Service Management API (https://cloud.google.com/service-management/overview). |
| `runtimeMainExecutablePath` | `string` | The path or name of the app's main executable. |
| `env` | `string` | App Engine execution environment for this version.Defaults to standard. |
| `resources` | `object` | Machine resources for a version. |
| `entrypoint` | `object` | The entrypoint for the application. |
| `defaultExpiration` | `string` | Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding StaticFilesHandler (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StaticFilesHandler) does not specify its own expiration time.Only returned in GET requests if view=FULL is set. |
| `instanceClass` | `string` | Instance class that is used to run this version. Valid values are: AutomaticScaling: F1, F2, F4, F4_1G ManualScaling or BasicScaling: B1, B2, B4, B8, B4_1GDefaults to F1 for AutomaticScaling and B1 for ManualScaling or BasicScaling. |
| `network` | `object` | Extra network settings. Only applicable in the App Engine flexible environment. |
| `deployment` | `object` | Code and application artifacts used to deploy a version to App Engine. |
| `readinessCheck` | `object` | Readiness checking configuration for VM instances. Unhealthy instances are removed from traffic rotation. |
| `vpcAccessConnector` | `object` | VPC access connector specification. |
| `automaticScaling` | `object` | Automatic scaling is based on request rate, response latencies, and other application metrics. |
| `basicScaling` | `object` | A service with basic scaling will create an instance when the application receives a request. The instance will be turned down when the app becomes idle. Basic scaling is ideal for work that is intermittent or driven by user activity. |
| `errorHandlers` | `array` | Custom static error pages. Limited to 10KB per page.Only returned in GET requests if view=FULL is set. |
| `createdBy` | `string` | Email address of the user who created this version.@OutputOnly |
| `handlers` | `array` | An ordered list of URL-matching patterns that should be applied to incoming requests. The first matching URL handles the request and other request handlers are not attempted.Only returned in GET requests if view=FULL is set. |
| `nobuildFilesRegex` | `string` | Files that match this pattern will not be built into this version. Only applicable for Go runtimes.Only returned in GET requests if view=FULL is set. |
| `appEngineApis` | `boolean` | Allows App Engine second generation runtimes to access the legacy bundled services. |
| `servingStatus` | `string` | Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.SERVING_STATUS_UNSPECIFIED is an invalid value. Defaults to SERVING. |
| `createTime` | `string` | Time that this version was created.@OutputOnly |
| `diskUsageBytes` | `string` | Total size in bytes of all the files that are included in this version and currently hosted on the App Engine disk.@OutputOnly |
| `healthCheck` | `object` | Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances. Only applicable for instances in App Engine flexible environment. |
| `serviceAccount` | `string` | The identity that the deployed version will run as. Admin API will use the App Engine Appspot service account as default if this field is neither provided in app.yaml file nor through CLI flag. |
| `inboundServices` | `array` | Before an application can receive email or XMPP messages, the application must be configured to enable the service. |
| `threadsafe` | `boolean` | Whether multiple requests can be dispatched to this version at once. |
| `betaSettings` | `object` | Metadata settings that are supplied to this version to enable beta runtime features. |
| `apiConfig` | `object` | Google Cloud Endpoints (https://cloud.google.com/appengine/docs/python/endpoints/) configuration for API handlers. |
| `buildEnvVariables` | `object` | Environment variables available to the build environment.Only returned in GET requests if view=FULL is set. |
| `zones` | `array` | The Google Compute Engine zones that are supported by this version in the App Engine flexible environment. Deprecated. |
| `vm` | `boolean` | Whether to deploy this version in a container on a virtual machine. |
| `manualScaling` | `object` | A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time. |
| `runtime` | `string` | Desired runtime. Example: python27. |
| `runtimeApiVersion` | `string` | The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at https://cloud.google.com/appengine/docs/standard//config/appref |
| `versionUrl` | `string` | Serving URL for this version. Example: "https://myversion-dot-myservice-dot-myapp.appspot.com"@OutputOnly |
| `livenessCheck` | `object` | Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `apps_services_versions_get` | `SELECT` | `appsId, servicesId, versionsId` | Gets the specified Version resource. By default, only a BASIC_VIEW will be returned. Specify the FULL_VIEW parameter to get the full resource. |
| `apps_services_versions_list` | `SELECT` | `appsId, servicesId` | Lists the versions of a service. |
| `apps_services_versions_create` | `INSERT` | `appsId, servicesId` | Deploys code and resource files to a new version. |
| `apps_services_versions_delete` | `DELETE` | `appsId, servicesId, versionsId` | Deletes an existing Version resource. |
| `apps_services_versions_patch` | `EXEC` | `appsId, servicesId, versionsId` | Updates the specified Version resource. You can specify the following fields depending on the App Engine environment and type of scaling that the version resource uses:Standard environment instance_class (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.instance_class)automatic scaling in the standard environment: automatic_scaling.min_idle_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.max_idle_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automaticScaling.standard_scheduler_settings.max_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.min_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.target_cpu_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.target_throughput_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)basic scaling or manual scaling in the standard environment: serving_status (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status) manual_scaling.instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#manualscaling)Flexible environment serving_status (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status)automatic scaling in the flexible environment: automatic_scaling.min_total_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.max_total_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.cool_down_period_sec (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.cpu_utilization.target_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)manual scaling in the flexible environment: manual_scaling.instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#manualscaling) |
