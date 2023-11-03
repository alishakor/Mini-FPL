var CreateTeam = (function () {
  let players = []
  let playerMap = new Map()
  let budget = 100
  let selectedPlayers = []
  let previousOption = {}

  function init(pls) {
    players = pls
    players.forEach(function (player) {
      playerMap.set(player.id, player)
    })
    setDropDown()
    setBudget(0)
    events()
  }

  function setDropDown() {
    players.forEach(function (player) {
      $('.testing').append(
        $('<option>', {
          value: player.id,
          text: `${player.name} ${player.position} ($${player.cost})`,
        }),
      )
    })

    $('.testing').on('change', function () {
      var selectedOption = $(this).val()

      // remove the selected option from all other dropdowns
      if (selectedOption !== '') {
        const selectedPlayer = playerMap.get(selectedOption)
        if (budget - selectedPlayer.cost < 0) {
          alert('Not enough budget')
          $(this).val('')
          return
        }

        setBudget(selectedPlayer.cost)

        // edit image
        const cardId = $(this).attr('id').split('-')[2]
        $(`#image-${cardId}`).attr('src', selectedPlayer.image)

        // edit cost
        $(`#price-${cardId}`).text(`$${selectedPlayer.cost}`)

        $('.testing')
          .not(this)
          .find('option[value="' + selectedOption + '"]')
          .remove()

        selectedPlayers.push(selectedOption)
      } else {
        const cardId = $(this).attr('id').split('-')[2]
        $(`#image-${cardId}`).attr('src', '../static/images/jersey.png')
        $(`#price-${cardId}`).text(`$0.0`)
      }

      // add back the previous option to the top of all dropdowns
      if (previousOption[$(this).attr('id')]) {
        po = previousOption[$(this).attr('id')]
        setBudget(-playerMap.get(po).cost)
        $('.testing')
          .not(this)
          .append(
            $('<option>', {
              value: po,
              text: `${playerMap.get(po).name} ${
                playerMap.get(po).position
              } ($${playerMap.get(po).cost})`,
            }),
          )

        selectedPlayers = selectedPlayers.filter(function (value) {
          return value !== po
        })
      }

      previousOption[$(this).attr('id')] = selectedOption
      $('#playersHidden').val(selectedPlayers.join(','))
    })
  }

  function setBudget(cost) {
    budget = budget - cost
    $('#budget').text(`$${budget}`)
  }

  function events() {
    $('#resetBtn').on('click', function () {
      $('.testing').val('')
      $('.testing').trigger('change')
      budget = 100
      selectedPlayers = []
      $('#budget').text(`$100`)
      $('#playersHidden').val('')
    })

    // check for change in value of input
    $('#teamName').on('input', function () {
      // update the value of #teamNameHidden
      $('#teamNameHidden').val($(this).val())
    })
  }

  return {
    _init: function (pls) {
      init(pls)
    },
  }
})()

var PickTeam = (function () {
  let startingPlayers = []
  let benchPlayers = []
  let playerMap = new Map()
  let startingPlayersIds = []
  let benchPlayersIds = []
  let previousOption = {}

  function init(team) {
    startingPlayers = team.starting_players
    benchPlayers = team.bench_players
    team.players.forEach(function (player) {
      playerMap.set(player.id, player)
    })
    startingPlayers.forEach(function (player) {
      startingPlayersIds.push(player.id)
    })
    benchPlayers.forEach(function (player) {
      benchPlayersIds.push(player.id)
    })
    $('#startingPlayersHidden').val(startingPlayersIds.join(','))
    $('#benchPlayersHidden').val(benchPlayersIds.join(','))
    setStartingPlayers()
    setBenchPlayers()
    events()
  }

  function setStartingPlayers() {
    startingPlayers.forEach(function (player) {
      $(`#image-${player.position}`).attr('src', player.image)
      $(`#price-${player.position}`).text(`$${player.cost}`)
    })

    for (let i = 0; i < startingPlayers.length; i++) {
      const player = startingPlayers[i]
      $(`#image-${i + 1}`).attr('src', player.image)
      $(`#player-name-${i + 1}`).append(
        $('<option>', {
          value: player.id,
          text: `${player.name} (${player.position})`,
        }),
      )

      previousOption[`player-name-${i + 1}`] = player.id

      // add all other players to each dropdown
      playerMap.forEach(function (value, key) {
        if (player.id !== value.id) {
          $(`#player-name-${i + 1}`).append(
            $('<option>', {
              value: value.id,
              text: `${value.name} (${value.position})`,
            }),
          )
        }
      })

      $(`#position-${i + 1}`).text(player.position)
    }
  }

  function setBenchPlayers() {
    for (let i = 0; i < benchPlayers.length; i++) {
      const player = benchPlayers[i]
      $(`#image-${i + 12}`).attr('src', player.image)
      $(`#player-name-${i + 12}`).append(
        $('<option>', {
          value: player.id,
          text: `${player.name} (${player.position})`,
        }),
      )
      $(`#position-${i + 12}`).text(player.position)

      previousOption[`player-name-${i + 12}`] = player.id

      // add all other players to each dropdown
      playerMap.forEach(function (value, key) {
        if (player.id !== value.id) {
          $(`#player-name-${i + 12}`).append(
            $('<option>', {
              value: value.id,
              text: `${value.name} (${value.position})`,
            }),
          )
        }
      })
    }
  }

  function GetStatus(id) {
    if (startingPlayersIds.includes(id)) {
      return 'starting'
    } else {
      return 'bench'
    }
  }

  function events() {
    $('.testing').on('change', function () {
      let selectedOption = $(this).val()
      let previousOpt = previousOption[$(this).attr('id')]

      let selectedStatus = GetStatus(selectedOption)
      let previousStatus = GetStatus(previousOpt)

      if (selectedStatus === 'starting' && previousStatus === 'starting') {
        // swap players
        let previous_opt_index = startingPlayersIds.indexOf(previousOpt)
        let selected_opt_index = startingPlayersIds.indexOf(selectedOption)

        let temp = startingPlayersIds[previous_opt_index]
        startingPlayersIds[previous_opt_index] =
          startingPlayersIds[selected_opt_index]
        startingPlayersIds[selected_opt_index] = temp

        // update previous option
        previousOption[$(this).attr('id')] = selectedOption

        // update elements
        $(`#image-${previous_opt_index + 1}`).attr(
          'src',
          playerMap.get(selectedOption).image,
        )
        $(`#player-name-${previous_opt_index + 1}`).val(selectedOption)
        $(`#position-${previous_opt_index + 1}`).text(
          playerMap.get(selectedOption).position,
        )

        $(`#image-${selected_opt_index + 1}`).attr(
          'src',
          playerMap.get(previousOpt).image,
        )
        $(`#player-name-${selected_opt_index + 1}`).val(previousOpt)
        $(`#position-${selected_opt_index + 1}`).text(
          playerMap.get(previousOpt).position,
        )
      } else if (selectedStatus === 'bench' && previousStatus === 'bench') {
        // swap players
        let previous_opt_index = benchPlayersIds.indexOf(previousOpt)
        let selected_opt_index = benchPlayersIds.indexOf(selectedOption)

        let temp = benchPlayersIds[previous_opt_index]
        benchPlayersIds[previous_opt_index] =
          benchPlayersIds[selected_opt_index]
        benchPlayersIds[selected_opt_index] = temp

        // update previous option
        previousOption[$(this).attr('id')] = selectedOption

        // update elements
        $(`#image-${previous_opt_index + 12}`).attr(
          'src',
          playerMap.get(selectedOption).image,
        )
        $(`#player-name-${previous_opt_index + 12}`).val(selectedOption)
        $(`#position-${previous_opt_index + 12}`).text(
          playerMap.get(selectedOption).position,
        )

        $(`#image-${selected_opt_index + 12}`).attr(
          'src',
          playerMap.get(previousOpt).image,
        )
        $(`#player-name-${selected_opt_index + 12}`).val(previousOpt)
        $(`#position-${selected_opt_index + 12}`).text(
          playerMap.get(previousOpt).position,
        )
      } else if (selectedStatus === 'starting' && previousStatus === 'bench') {
        // swap players
        let previous_opt_index = benchPlayersIds.indexOf(previousOpt)
        let selected_opt_index = startingPlayersIds.indexOf(selectedOption)

        let temp = benchPlayersIds[previous_opt_index]
        benchPlayersIds[previous_opt_index] =
          startingPlayersIds[selected_opt_index]
        startingPlayersIds[selected_opt_index] = temp

        // update previous option
        previousOption[$(this).attr('id')] = selectedOption

        // update elements
        $(`#image-${previous_opt_index + 12}`).attr(
          'src',
          playerMap.get(selectedOption).image,
        )
        $(`#player-name-${previous_opt_index + 12}`).val(selectedOption)
        $(`#position-${previous_opt_index + 12}`).text(
          playerMap.get(selectedOption).position,
        )

        $(`#image-${selected_opt_index + 1}`).attr(
          'src',
          playerMap.get(previousOpt).image,
        )
        $(`#player-name-${selected_opt_index + 1}`).val(previousOpt)
        $(`#position-${selected_opt_index + 1}`).text(
          playerMap.get(previousOpt).position,
        )
      } else if (selectedStatus === 'bench' && previousStatus === 'starting') {
        // swap players
        let previous_opt_index = startingPlayersIds.indexOf(previousOpt)
        let selected_opt_index = benchPlayersIds.indexOf(selectedOption)

        let temp = startingPlayersIds[previous_opt_index]
        startingPlayersIds[previous_opt_index] =
          benchPlayersIds[selected_opt_index]
        benchPlayersIds[selected_opt_index] = temp

        // update previous option
        previousOption[$(this).attr('id')] = selectedOption

        // update elements
        $(`#image-${previous_opt_index + 1}`).attr(
          'src',
          playerMap.get(selectedOption).image,
        )
        $(`#player-name-${previous_opt_index + 1}`).val(selectedOption)
        $(`#position-${previous_opt_index + 1}`).text(
          playerMap.get(selectedOption).position,
        )

        $(`#image-${selected_opt_index + 12}`).attr(
          'src',
          playerMap.get(previousOpt).image,
        )
        $(`#player-name-${selected_opt_index + 12}`).val(previousOpt)
        $(`#position-${selected_opt_index + 12}`).text(
          playerMap.get(previousOpt).position,
        )
      }

      $('#startingPlayersHidden').val(startingPlayersIds.join(','))
      $('#benchPlayersHidden').val(benchPlayersIds.join(','))
    })
  }

  return {
    _init: function (pls) {
      init(pls)
    },
  }
})()
