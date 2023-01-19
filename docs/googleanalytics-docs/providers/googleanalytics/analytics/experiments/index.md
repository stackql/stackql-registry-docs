---
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments
  - analytics
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.experiments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Experiment ID. Required for patch and update. Disallowed for create. |
| `name` | `string` | Experiment name. This field may not be changed for an experiment whose status is ENDED. This field is required when creating an experiment. |
| `description` | `string` | Notes about this experiment. |
| `winnerConfidenceLevel` | `number` | A floating-point number in (0, 1). Specifies the necessary confidence level to choose a winner. This field may not be changed for an experiments whose status is ENDED. |
| `reasonExperimentEnded` | `string` | Why the experiment ended. Possible values: "STOPPED_BY_USER", "WINNER_FOUND", "EXPERIMENT_EXPIRED", "ENDED_WITH_NO_WINNER", "GOAL_OBJECTIVE_CHANGED". "ENDED_WITH_NO_WINNER" means that the experiment didn't expire but no winner was projected to be found. If the experiment status is changed via the API to ENDED this field is set to STOPPED_BY_USER. This field is read-only. |
| `servingFramework` | `string` | The framework used to serve the experiment variations and evaluate the results. One of:  <br />- REDIRECT: Google Analytics redirects traffic to different variation pages, reports the chosen variation and evaluates the results.<br />- API: Google Analytics chooses and reports the variation to serve and evaluates the results; the caller is responsible for serving the selected variation.<br />- EXTERNAL: The variations will be served externally and the chosen variation reported to Google Analytics. The caller is responsible for serving the selected variation and evaluating the results. |
| `startTime` | `string` | The starting time of the experiment (the time the status changed from READY_TO_RUN to RUNNING). This field is present only if the experiment has started. This field is read-only. |
| `optimizationType` | `string` | Whether the objectiveMetric should be minimized or maximized. Possible values: "MAXIMUM", "MINIMUM". Optional--defaults to "MAXIMUM". Cannot be specified without objectiveMetric. Cannot be modified when status is "RUNNING" or "ENDED". |
| `webPropertyId` | `string` | Web property ID to which this experiment belongs. The web property ID is of the form UA-XXXXX-YY. This field is read-only. |
| `parentLink` | `object` | Parent link for an experiment. Points to the view (profile) to which this experiment belongs. |
| `objectiveMetric` | `string` | The metric that the experiment is optimizing. Valid values: "ga:goal(n)Completions", "ga:adsenseAdsClicks", "ga:adsenseAdsViewed", "ga:adsenseRevenue", "ga:bounces", "ga:pageviews", "ga:sessionDuration", "ga:transactions", "ga:transactionRevenue". This field is required if status is "RUNNING" and servingFramework is one of "REDIRECT" or "API". |
| `equalWeighting` | `boolean` | Boolean specifying whether to distribute traffic evenly across all variations. If the value is False, content experiments follows the default behavior of adjusting traffic dynamically based on variation performance. Optional -- defaults to False. This field may not be changed for an experiment whose status is ENDED. |
| `endTime` | `string` | The ending time of the experiment (the time the status changed from RUNNING to ENDED). This field is present only if the experiment has ended. This field is read-only. |
| `snippet` | `string` | The snippet of code to include on the control page(s). This field is read-only. |
| `profileId` | `string` | View (Profile) ID to which this experiment belongs. This field is read-only. |
| `internalWebPropertyId` | `string` | Internal ID for the web property to which this experiment belongs. This field is read-only. |
| `rewriteVariationUrlsAsOriginal` | `boolean` | Boolean specifying whether variations URLS are rewritten to match those of the original. This field may not be changed for an experiments whose status is ENDED. |
| `created` | `string` | Time the experiment was created. This field is read-only. |
| `accountId` | `string` | Account ID to which this experiment belongs. This field is read-only. |
| `selfLink` | `string` | Link for this experiment. This field is read-only. |
| `updated` | `string` | Time the experiment was last modified. This field is read-only. |
| `status` | `string` | Experiment status. Possible values: "DRAFT", "READY_TO_RUN", "RUNNING", "ENDED". Experiments can be created in the "DRAFT", "READY_TO_RUN" or "RUNNING" state. This field is required when creating an experiment. |
| `editableInGaUi` | `boolean` | If true, the end user will be able to edit the experiment via the Google Analytics user interface. |
| `minimumExperimentLengthInDays` | `integer` | An integer number in [3, 90]. Specifies the minimum length of the experiment. Can be changed for a running experiment. This field may not be changed for an experiments whose status is ENDED. |
| `kind` | `string` | Resource type for an Analytics experiment. This field is read-only. |
| `variations` | `array` | Array of variations. The first variation in the array is the original. The number of variations may not change once an experiment is in the RUNNING state. At least two variations are required before status can be set to RUNNING. |
| `trafficCoverage` | `number` | A floating-point number in (0, 1]. Specifies the fraction of the traffic that participates in the experiment. Can be changed for a running experiment. This field may not be changed for an experiments whose status is ENDED. |
| `winnerFound` | `boolean` | Boolean specifying whether a winner has been found for this experiment. This field is read-only. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `management_experiments_get` | `SELECT` | `accountId, experimentId, profileId, webPropertyId` | Returns an experiment to which the user has access. |
| `management_experiments_list` | `SELECT` | `accountId, profileId, webPropertyId` | Lists experiments to which the user has access. |
| `management_experiments_delete` | `DELETE` | `accountId, experimentId, profileId, webPropertyId` | Delete an experiment. |
| `management_experiments_insert` | `EXEC` | `accountId, profileId, webPropertyId` | Create a new experiment. |
| `management_experiments_patch` | `EXEC` | `accountId, experimentId, profileId, webPropertyId` | Update an existing experiment. This method supports patch semantics. |
| `management_experiments_update` | `EXEC` | `accountId, experimentId, profileId, webPropertyId` | Update an existing experiment. |
