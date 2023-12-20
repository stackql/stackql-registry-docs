---
title: pagerduty
hide_title: false
hide_table_of_contents: false
keywords:
  - pagerduty
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
id: pagerduty-doc
slug: /providers/pagerduty

---
Incident management platform for real-time operations and response workflows.  
    
:::info Provider Summary (v23.12.00190)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>33</b></span><br />
<span>total methods:&nbsp;<b>438</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>100</b></span><br />
<span>total selectable resources:&nbsp;<b>98</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `pagerduty` provider, run the following command:  

```bash
REGISTRY PULL pagerduty;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- `PAGERDUTY_API_TOKEN` - PagerDuty API token (see [Creating a PagerDuty API Token](https://support.pagerduty.com/docs/api-access-keys#section-generating-a-general-access-rest-api-key))
  
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "pagerduty": { "type": "bearer", "credentialsenvvar": "YOUR_PAGERDUTY_API_TOKEN_VAR" }}'
stackql shell --auth="${AUTH}"

```
or using PowerShell:  

```powershell

$Auth = "{ 'pagerduty': { 'type': 'bearer', 'credentialsenvvar': 'YOUR_PAGERDUTY_API_TOKEN_VAR' }}"
stackql.exe shell --auth=$Auth

```
</details>

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/pagerduty/abilities/">abilities</a><br />
<a href="/providers/pagerduty/add_ons/">add_ons</a><br />
<a href="/providers/pagerduty/analytics/">analytics</a><br />
<a href="/providers/pagerduty/audit/">audit</a><br />
<a href="/providers/pagerduty/automation_actions/">automation_actions</a><br />
<a href="/providers/pagerduty/business_services/">business_services</a><br />
<a href="/providers/pagerduty/change_events/">change_events</a><br />
<a href="/providers/pagerduty/custom_fields/">custom_fields</a><br />
<a href="/providers/pagerduty/escalation_policies/">escalation_policies</a><br />
<a href="/providers/pagerduty/event_orchestrations/">event_orchestrations</a><br />
<a href="/providers/pagerduty/extension_schemas/">extension_schemas</a><br />
<a href="/providers/pagerduty/extensions/">extensions</a><br />
<a href="/providers/pagerduty/incident_workflows/">incident_workflows</a><br />
<a href="/providers/pagerduty/incidents/">incidents</a><br />
<a href="/providers/pagerduty/licenses/">licenses</a><br />
<a href="/providers/pagerduty/log_entries/">log_entries</a><br />
<a href="/providers/pagerduty/maintenance_windows/">maintenance_windows</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/pagerduty/notifications/">notifications</a><br />
<a href="/providers/pagerduty/on_calls/">on_calls</a><br />
<a href="/providers/pagerduty/paused_incident_reports/">paused_incident_reports</a><br />
<a href="/providers/pagerduty/priorities/">priorities</a><br />
<a href="/providers/pagerduty/response_plays/">response_plays</a><br />
<a href="/providers/pagerduty/rulesets/">rulesets</a><br />
<a href="/providers/pagerduty/schedules/">schedules</a><br />
<a href="/providers/pagerduty/service_dependencies/">service_dependencies</a><br />
<a href="/providers/pagerduty/services/">services</a><br />
<a href="/providers/pagerduty/status_dashboards/">status_dashboards</a><br />
<a href="/providers/pagerduty/tags/">tags</a><br />
<a href="/providers/pagerduty/teams/">teams</a><br />
<a href="/providers/pagerduty/templates/">templates</a><br />
<a href="/providers/pagerduty/users/">users</a><br />
<a href="/providers/pagerduty/vendors/">vendors</a><br />
<a href="/providers/pagerduty/webhooks/">webhooks</a><br />
</div>
</div>
